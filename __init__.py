import logging
from os.path import join
from utils.logger import log_dir


# Create a root_logger for the package
logger = logging.getLogger(__name__)


def configure_logger() -> None:
    """
    Set up the package root_logger.

    :return: None.
    """

    # Set the logging level to INFO
    #logger.setLevel(logging.INFO)

    # Create a handler to write log messages to a file
    handler = logging.FileHandler(join(log_dir, __name__ + '.log'))

    # Create a formatter to format log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the console handler to the root_logger
    logger.addHandler(handler)

# Call the configuration function to set up the root_logger
configure_logger()
