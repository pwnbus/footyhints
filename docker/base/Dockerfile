FROM ubuntu:latest

RUN \
  apt-get update --fix-missing && \
  apt-get upgrade -y && \
  apt-get install -y --fix-missing \
    python3 \
    python3-pip && \
  ln -s /usr/bin/python3 /usr/bin/python && \
  apt-get clean all && \
  mkdir /app && \
  mkdir /app/data

COPY setup.py /app/setup.py
COPY footyhints /app/footyhints

WORKDIR /app

RUN pip3 install -e .

COPY docker/base/files/config.inc /app/config.txt
