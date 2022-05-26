#!/bin/sh

echo "Waiting for mongodb..."

while ! nc -z mongo 27017; 
do
	sleep 0.1
done
echo "Mongodb started"

python3 app.py
exec "$@"
