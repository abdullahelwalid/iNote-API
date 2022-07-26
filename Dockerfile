FROM python:3.8-slim-buster

# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /note_api

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DB_VAR="root:Abood2004@127.0.0.1:3306/inote"
# Install any dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "flask", "run" ]