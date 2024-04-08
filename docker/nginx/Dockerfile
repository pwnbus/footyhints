FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y nginx curl && \
  rm -rf /var/lib/apt/lists/*

COPY docker/nginx/files/start.sh /start.sh

RUN \
  chmod u+x /start.sh && \
  echo "daemon off;" >> /etc/nginx/nginx.conf && \
  rm /etc/nginx/sites-enabled/* && \
  mkdir -p /etc/nginx/ssl/live/localhost && \
  mkdir -p /etc/nginx/ssl/preloaded

COPY docker/nginx/files/localhost.crt /etc/nginx/ssl/preloaded/localhost.crt
COPY docker/nginx/files/localhost.key /etc/nginx/ssl/preloaded/localhost.key

COPY docker/nginx/files/web.conf /etc/nginx/sites-enabled/web.conf

VOLUME /etc/nginx/ssl/live/

EXPOSE 80

CMD /start.sh
