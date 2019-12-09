FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y nginx && \
  rm -rf /var/lib/apt/lists/*

RUN \
  echo "daemon off;" >> /etc/nginx/nginx.conf && \
  rm /etc/nginx/sites-enabled/*

COPY docker/nginx/files/flask.conf /etc/nginx/sites-enabled/flask.conf

EXPOSE 80

CMD '/usr/sbin/nginx'
