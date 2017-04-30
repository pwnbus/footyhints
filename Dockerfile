from ubuntu:latest

USER root
RUN apt-get install -y python3.5 wget git python3.5-dev build-essential
RUN useradd -m footyhints
RUN wget -O /root/get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python3.5 /root/get-pip.py
RUN rm /root/get-pip.py
RUN pip install virtualenv
USER footyhints
RUN mkdir /home/footyhints/scoring_engine
RUN virtualenv -p /usr/bin/python3.5 /home/footyhints/scoring_engine/env
RUN git clone https://github.com/pwnbus/scoring_engine /home/engine/scoring_engine/src
RUN source /home/engine/scoring_engine/env/bin/activate
RUN pip install -e /home/engine/scoring_engine/src/
RUN id
