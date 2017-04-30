from ubuntu:latest

USER root
RUN apt-get update
RUN apt-get install -y python3.5 wget git python3.5-dev build-essential
RUN useradd -m footyhints
RUN wget -O /root/get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python3.5 /root/get-pip.py
RUN rm /root/get-pip.py
RUN pip install virtualenv
USER footyhints
RUN mkdir /home/footyhints/footyhints
RUN virtualenv -p /usr/bin/python3.5 /home/footyhints/footyhints/env
RUN mkdir ~/.ssh
RUN chmod 700 ~/.ssh
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
RUN git clone https://github.com/pwnbus/footyhints /home/footyhints/footyhints/src
RUN cd /home/footyhints/footyhints/src;git pull origin master
RUN /bin/bash -c "source /home/footyhints/footyhints/env/bin/activate;pip install -e /home/footyhints/footyhints/src/"
RUN sed -i -e 's/DEBUG = False/DEBUG = True/g' /home/footyhints/footyhints/src/footyhints/web/settings.cfg

CMD /bin/bash -c "source /home/footyhints/footyhints/env/bin/activate;cd /home/footyhints/footyhints/src/;python run.py"
