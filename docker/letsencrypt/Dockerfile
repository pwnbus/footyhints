FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y nginx curl supervisor cron certbot && \
  rm -rf /var/lib/apt/lists/*

COPY docker/letsencrypt/files/start.sh /start.sh
COPY docker/letsencrypt/files/generate_cert.sh /generate_cert.sh

COPY docker/letsencrypt/files/supervisord.conf /etc/supervisor/supervisord.conf

RUN \
  chmod u+x /start.sh && \
  chmod u+x /generate_cert.sh && \
  echo "daemon off;" >> /etc/nginx/nginx.conf && \
  rm /etc/nginx/sites-enabled/* && \
  mkdir -p /etc/nginx/certs/preloaded

COPY docker/letsencrypt/files/localhost_fullchain.pem /etc/nginx/preloaded/fullchain.pem
COPY docker/letsencrypt/files/localhost_privkey.pem /etc/nginx/preloaded/privkey.pem

COPY docker/letsencrypt/files/web.conf /etc/nginx/sites-enabled/web.conf

EXPOSE 80
EXPOSE 443

CMD /start.sh
