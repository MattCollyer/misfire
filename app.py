#!/usr/bin/env python3
"""
	Author: Matthew Collyer (matthewcollyer@bennington.edu)
	Date: May 2 2018
"""
from flask import Flask, render_template, request
from pymongo import MongoClient
import random
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/doodle', methods=['POST'])
def doodle():
	return render_template('doodle.html', doodle=get_doodle())

@app.route('/lookup',methods=['GET'])
def lookup():
	return render_template('lookup.html')

@app.route('/lookup/doodle',methods=['POST'])
def doodle_lookup():
	id=request.form['lookup']
	doodle=get_doodle(int(id))
	return render_template('doodle_lookup.html',doodle=doodle)

@app.route('/reveal/<key_id>',methods=['POST'])
def reveal(key_id):
	guess=request.form['guess']
	guess=guess.strip()
	correct=True
	doodle=get_doodle(int(key_id))
	if(guess.lower()!=doodle['word'].lower()):
		correct=False
	update_table(int(key_id),guess,correct)
	h1="Correct!"
	h3="It still benefits to be human"
	if(correct==False):
		h1="Incorrect!"
		h3="Sorry, but you're no better than the neural network!"
	return render_template('reveal.html',doodle=doodle,correct=correct,head1=h1,head3=h3)

def get_doodle(key_id=None):
	"""
	Returns a random doodle object from mongoDB.
	"""
	try:
		# client = MongoClient('localhost')
		client = MongoClient('mongodb',27017) # get our client
		db = client.quickdraw # get our database
		if(key_id==None): #if random
			total=db.qd.count()
			rando=random.randint(1,total)
			doodle=db.qd.find_one({'key_id':rando})
		else:
			doodle=db.qd.find_one({'key_id':key_id})
		return doodle
	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

def update_table(key_id,guess,correct):
	"""
	Updates the db
	if wrong: adds guess
	if right: adds +1 for right guesses
	"""
	try:
		#client =MongoClient('localhost')
		client = MongoClient('mongodb',27017) # get our client
		db = client.quickdraw # get our database
		if(correct==False):
			if(guess!=""):
				db.qd.update_one({'key_id':key_id},{'$push': {'human_guesses': guess}})
		else:
			db.qd.update_one({'key_id':key_id},{'$inc':{'recognized_by_human': 1}})
	except Exception as e:
		print("Unable to connect to database: {0}".format(e))

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80)
