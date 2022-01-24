#!/bin/bash

apt-get update && apt-get install -y python3 python3.8-venv bash python3-pip

python3 -m venv venv
. venv/bin/activate
pip3 install Flask
pip3 install flask-cors
export FLASK_APP=hello
export FLASK_ENV=development
flask run --host=0.0.0.0
