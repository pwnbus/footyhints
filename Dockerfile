FROM ubuntu:latest

RUN apt-get update --fix-missing
RUN apt-get install -y python3.5 wget python3.5-dev build-essential
RUN wget -O /root/get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python3.5 /root/get-pip.py
RUN rm /root/get-pip.py

COPY . /app
WORKDIR /app
RUN cp config.txt.inc config.txt
RUN sed -i -e 's/debug = True/debug = False/g' config.txt

RUN pip install -e .

CMD /bin/bash -c "python3.5 bin/import_pl_data;python3.5 run.py"

