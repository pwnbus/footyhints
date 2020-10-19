import logging

logger = logging.getLogger('footyhints')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def set_logger_debug():
    logger.setLevel(logging.DEBUG)
