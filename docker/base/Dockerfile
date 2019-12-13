FROM ubuntu:latest

RUN \
  apt-get update --fix-missing && \
  apt-get upgrade -y && \
  apt-get install -y --fix-missing \
    python3 \
    python3-pip \
    libssl-dev \
    libmysqlclient-dev && \
  apt-get clean all && \
  rm -rf /var/lib/apt/lists/* && \
  pip3 install virtualenv && \
  useradd --create-home --shell /bin/bash --home-dir /opt/footyhints footyhints && \
  mkdir -p /opt/footyhints/envs/footyhints && \
  chown -R footyhints:footyhints /opt/footyhints/envs

USER footyhints

COPY --chown=footyhints:footyhints docker/wait-for-container.sh /opt/footyhints/envs/footyhints/wait-for-container.sh
COPY --chown=footyhints:footyhints docker/wait-for-port.sh /opt/footyhints/envs/footyhints/wait-for-port.sh

RUN virtualenv -p `which python3` /opt/footyhints/envs/python

# Automatically source into python virtual environment
ENV PATH=/opt/footyhints/envs/python/bin:$PATH

COPY --chown=footyhints:footyhints setup.py /opt/footyhints/envs/footyhints/setup.py
COPY --chown=footyhints:footyhints footyhints /opt/footyhints/envs/footyhints/footyhints

RUN pip install -e /opt/footyhints/envs/footyhints

WORKDIR /opt/footyhints/envs/footyhints
