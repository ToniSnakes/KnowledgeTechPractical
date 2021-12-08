#!/bin/bash

#docker tag privates tonisnakes/privates
docker buildx build --platform linux/arm/v7 -t tonisnakes/privates:ktp-frontend-arm .
docker push tonisnakes/privates:ktp-frontend-arm
