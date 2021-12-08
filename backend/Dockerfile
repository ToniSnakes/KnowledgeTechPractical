#FROM ubuntu:latest
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3.8-venv bash python3-pip

COPY hello.py /
COPY init_backend.sh /
#COPY init_backend-arm.sh /
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install Flask
RUN pip3 install flask-cors
ENTRYPOINT [ "bash", "/init_backend.sh" ]
#ENTRYPOINT [ "bash", "/init_backend-arm.sh" ]
#ENTRYPOINT [ "sleep", "604800" ]
