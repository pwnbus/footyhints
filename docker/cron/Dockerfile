FROM footyhints/footyhints_base:latest

USER root

RUN \
  apt-get update --fix-missing && \
  apt-get install -y --fix-missing cron && \
  rm -rf /var/lib/apt/lists/*

USER footyhints

COPY --chown=footyhints:footyhints bin/setup_db bin/setup_db
COPY --chown=footyhints:footyhints docker/cron/files/launch_cron /launch_cron
COPY --chown=footyhints:footyhints docker/cron/files/cron_entries.txt ./cron_entries.txt

RUN chmod u+x /launch_cron
RUN crontab ./cron_entries.txt

USER root

CMD ["./wait-for-container.sh", "bootstrap", "/launch_cron"]