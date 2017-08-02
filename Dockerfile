FROM ubuntu:latest

RUN \
  apt-get update --fix-missing && \
  apt-get upgrade -y && \
  apt-get install -y --fix-missing \
    python3.5 \
    python3.5-dev \
    build-essential \
    curl && \
  curl -o /root/get-pip.py https://bootstrap.pypa.io/get-pip.py && \
  python3.5 /root/get-pip.py && \
  rm /root/get-pip.py && \
  mkdir /app

COPY setup.py /app/setup.py
COPY footyhints /app/footyhints
WORKDIR /app

RUN pip install -e .

COPY config.txt.inc /app/config.txt
RUN sed -i -e 's/debug = True/debug = False/g' config.txt

COPY bin /app/bin
RUN python3.5 ./bin/create_sample_db

COPY run.py /app/run.py
CMD ["python3.5", "run.py"]

EXPOSE 5000
