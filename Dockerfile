FROM python:3.6
ADD . /misfire
WORKDIR /misfire
RUN pip3 install -r requirements.txt
# Make port available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
CMD ["python3", "app.py"]
