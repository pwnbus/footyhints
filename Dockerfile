FROM ubuntu:latest

RUN \
  apt-get update --fix-missing && \
  apt-get upgrade -y && \
  apt-get install -y --fix-missing \
    python3 \
    python3-pip && \
  apt-get clean all && \
  mkdir /app

COPY setup.py /app/setup.py
COPY footyhints /app/footyhints
WORKDIR /app

RUN pip3 install -e .

COPY config.txt.inc /app/config.txt
COPY bin /app/bin

ARG FOOTYHINTS_TYPE=development
ARG FOOTYHINTS_API_TOKEN=none

RUN \
  if printenv | grep "FOOTYHINTS_TYPE=production"; \
  then \
    python3 ./bin/import_pl_data; \
  else \
    python3 ./bin/create_sample_db; \
  fi

COPY run.py /app/run.py
CMD ["python3", "run.py"]

EXPOSE 5000
