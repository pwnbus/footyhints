#!/bin/bash

mkdir -p /etc/nginx/certs/live/default
cp /etc/nginx/preloaded/fullchain.pem /etc/nginx/certs/live/default/fullchain.pem
cp /etc/nginx/preloaded/privkey.pem /etc/nginx/certs/live/default/privkey.pem

/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
