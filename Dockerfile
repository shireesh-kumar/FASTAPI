FROM python:3.13-slim-bullseye

# Set the working directory
WORKDIR /app

COPY  . /app

RUN pip install -r requirements.txt

EXPOSE 8000

