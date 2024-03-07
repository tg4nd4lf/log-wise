from src.logger import *


class TestLogger:
    """
    Class for all tests of 'logger.py'.
    """

    def test_print_logs(self) -> None:
        """
        Print a few log messages.

        :return:
        """

        # prepare
        log = configure_logger()
        # print
        log.debug("Hello World!")
        log.info("Hello World!")
        log.warning("Hello World!")
        log.error("Hello World!")
        log.critical("Hello World!")


if __name__ == '__main__':
    print(__file__)
