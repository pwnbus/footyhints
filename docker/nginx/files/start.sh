#!/bin/bash

cp /etc/nginx/ssl/preloaded/localhost.crt /etc/nginx/ssl/live/localhost/localhost.crt
cp /etc/nginx/ssl/preloaded/localhost.key /etc/nginx/ssl/live/localhost/localhost.key

# Start nginx
/usr/sbin/nginx