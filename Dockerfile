from ubuntu:latest

USER root
RUN apt-get install -y python3.5 wget git python3.5-dev build-essential
RUN useradd -m footyhints
RUN wget -O /root/get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python3.5 /root/get-pip.py
RUN rm /root/get-pip.py
RUN pip install virtualenv
USER footyhints
RUN mkdir /home/footyhints/footyhints
RUN virtualenv -p /usr/bin/python3.5 /home/footyhints/footyhints/env
RUN git clone https://github.com/pwnbus/footyhints /home/footyhints/footyhints/src
RUN source /home/footyhints/footyhints/env/bin/activate
RUN pip install -e /home/footyhints/footyhints/src/
CMD id
