FROM footyhints_base:latest

ARG FOOTYHINTS_TYPE=development
ARG FOOTYHINTS_API_TOKEN=none

RUN \
  if printenv | grep "FOOTYHINTS_API=production"; \
  then \
    python3 ./bin/import_pl_data; \
  else \
    python3 ./bin/create_sample_db; \
  fi