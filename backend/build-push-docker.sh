#!/bin/bash

#docker tag privates tonisnakes/privates
docker build -t tonisnakes/privates:ktp-backend .
docker push tonisnakes/privates:ktp-backend
