# Use python base image
FROM python:3.8-slim-buster


WORKDIR /src

# Install dependencies
COPY ./src /src
COPY requirements.txt /src 
RUN pip3 install -r requirements.txt




CMD [ "python3", "main.py"]