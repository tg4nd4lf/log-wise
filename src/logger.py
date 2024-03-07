import os
import logging
import datetime
from formatter import CustomFormatter


def configure_logger() -> logging.Logger:
    """
    Set up logger.

    :return: Logger instance.
    """

    # Create custom logger logging all five levels
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define format for logs
    fmt = '%(asctime)s | %(levelname)8s | %(message)s'

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(CustomFormatter(fmt))

    # Create file handler for logging to a file (logs all five levels)
    today = datetime.date.today()

    file_handler = logging.FileHandler(filename=os.path.join(os.path.dirname(__file__), 'my_app_{}.log'.format(today.strftime('%Y_%m_%d'))))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(fmt))

    # Add both handlers to the logger
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    log = configure_logger()
    log.debug("Hello World!")
    log.info("Hello World!")
    log.warning("Hello World!")
    log.error("Hello World!")
    log.critical("Hello World!")
