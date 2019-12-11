FROM footyhints_base

COPY tests tests

COPY docker/tester/files/config.txt config.txt
COPY .flake8 .flake8

RUN pip install -r tests/requirements.txt
