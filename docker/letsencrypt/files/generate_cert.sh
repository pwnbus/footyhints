#!/bin/bash

set -e

echo "Removing placeholder certs"
rm -rf /etc/nginx/certs/live/default

echo "Generating cert for $FOOTYHINTS_URL"
certbot certonly --webroot --webroot-path=/var/www/html --config-dir /etc/nginx/certs/ --register-unsafely-without-email --agree-tos --no-eff-email -d $FOOTYHINTS_URL -d www.$FOOTYHINTS_URL --cert-name default

echo "Reloading nginx"
nginx -s reload
