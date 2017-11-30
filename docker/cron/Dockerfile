FROM footyhints_base:latest

RUN apt-get install -y cron

COPY bin /app/bin
COPY docker/cron/files/cron_entries.txt /cron_entries.txt

RUN crontab /cron_entries.txt
