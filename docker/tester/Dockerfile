FROM footyhints/footyhints_base

USER root

RUN \
  apt-get update && \
  apt-get install -y curl && \
  rm -rf /var/lib/apt/lists/* && \
  curl -s -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 -o /usr/bin/cc-test-reporter && \
  chmod +x /usr/bin/cc-test-reporter && \
  mkdir /opt/footyhints/envs/artifacts && \
  chown footyhints:footyhints /opt/footyhints/envs/artifacts

COPY --chown=footyhints:footyhints .flake8 .flake8

USER footyhints

COPY --chown=footyhints:footyhints ./tests tests

RUN pip install -r tests/requirements.txt

CMD ["./wait-for-port.sh", "mysql:3306", "py.test", "--cov=footyhints", "--cov-report=xml:/opt/footyhints/envs/artifacts/coverage.xml", "tests"]
