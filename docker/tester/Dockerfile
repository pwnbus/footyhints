FROM footyhints/footyhints_base:latest

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN \
  apt-get update && \
  apt-get install -y \
    curl \
    nodejs \
    npm && \
  rm -rf /var/lib/apt/lists/* && \
  curl -s -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 -o /usr/bin/cc-test-reporter && \
  chmod +x /usr/bin/cc-test-reporter && \
  mkdir /opt/footyhints/envs/artifacts && \
  chown footyhints:footyhints /opt/footyhints/envs/artifacts && \
  npm install htmlhint

COPY --chown=footyhints:footyhints .flake8 .flake8
COPY --chown=footyhints:footyhints .htmlhint .htmlhint
COPY --chown=footyhints:footyhints pytest.ini pytest.ini

USER footyhints

COPY --chown=footyhints:footyhints ./tests tests

RUN pip install -r tests/requirements.txt

CMD ["./wait-for-port.sh", "mysql:3306", "py.test", "--cov=footyhints", "--cov-report=xml:/opt/footyhints/envs/artifacts/coverage.xml", "tests"]
