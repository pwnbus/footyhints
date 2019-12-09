FROM footyhints_base

USER root

RUN \
  apt-get update --fix-missing && \
  apt-get install -y --fix-missing cron && \
  rm -rf /var/lib/apt/lists/*

USER footyhints

COPY --chown=footyhints:footyhints bin/setup_db bin/setup_db
COPY --chown=footyhints:footyhints docker/cron/files/cron_entries.txt ./cron_entries.txt

RUN crontab ./cron_entries.txt

CMD ["./wait-for-container.sh", "bootstrap", "cron -f"]