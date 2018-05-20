FROM mongo
COPY doods.json /doods.json
CMD mongoimport --host mongodb -d quickdraw -c qd --file doods.json
