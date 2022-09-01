FROM python:3.8-slim-buster

WORKDIR /note_api

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
ENV DB_VAR="root:Abood2004@127.0.0.1:3306/inote"
RUN pip install mysql-connector-python
EXPOSE 5000/tcp
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0" ]


# FROM python:3.8-slim-buster

# # Set the working directory in the container
# WORKDIR /note_api

# # Copy the dependencies file to the working directory
# COPY requirements.txt requirements.txt

# ENV FLASK_APP=main.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV DB_VAR="root:Abood2004@127.0.0.1:3306/inote"
# # Install any dependencies
# RUN python -m pip install --upgrade pip
# RUN pip install mysql-connector-python
# RUN pip install -r requirements.txt

# # Copy the content of the local src directory to the working directory
# COPY . .

# EXPOSE 5000/tcp

# # Specify the command to run on container start
# ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0" ]