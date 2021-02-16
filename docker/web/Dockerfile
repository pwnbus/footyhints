FROM footyhints/footyhints_base:latest

COPY --chown=footyhints:footyhints bin/web bin/web

EXPOSE 8000

CMD ["./wait-for-container.sh", "bootstrap", "./bin/web"]