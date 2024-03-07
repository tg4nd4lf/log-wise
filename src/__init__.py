import os
import logging


# Create a root_logger for the package
logger = logging.getLogger(__name__)


def configure_logger() -> None:
    """
    Set up the package root_logger.

    :return: None.
    """

    # Set the logging level to INFO
    logger.setLevel(logging.INFO)

    # Create a handler to write log messages to a file
    handler = logging.FileHandler(filename=os.path.join(os.path.dirname(__file__), 'my_app_{}.log'.format(today.strftime('%Y_%m_%d'))))

    # Create a formatter to format log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the console handler to the root_logger
    logger.addHandler(handler)


# Call the configuration function to set up the root_logger
configure_logger()
