FROM python:3.8-slim-buster

RUN apt update && apt install -y netcat

WORKDIR /app
COPY bot/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY entry.sh entry.sh

COPY bot/app.py app.py
COPY bot/db.py db.py

ENTRYPOINT /bin/bash entry.sh
