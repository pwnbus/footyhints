FROM footyhints_base

COPY --chown=footyhints:footyhints bin/setup_db bin/setup_db

CMD ["./wait-for-port.sh", "mysql:3306", "./bin/setup_db"]
