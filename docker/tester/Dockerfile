FROM footyhints_base

COPY tests tests

COPY docker/tester/files/config.txt config.txt
RUN pip install -r tests/requirements.txt
