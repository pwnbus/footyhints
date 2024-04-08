FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y nginx curl && \
  rm -rf /var/lib/apt/lists/*

RUN \
  echo "daemon off;" >> /etc/nginx/nginx.conf && \
  rm /etc/nginx/sites-enabled/*

COPY docker/nginx/files/web.conf /etc/nginx/sites-enabled/web.conf

EXPOSE 80

CMD '/usr/sbin/nginx'
