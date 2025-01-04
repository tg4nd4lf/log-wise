#!/usr/bin/env python3

# Filename: logger.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Logger. """

import logging
from pathlib import Path
from .formatter import CustomFormatter
from logging.handlers import TimedRotatingFileHandler

__version__ = "2.2"
__author__ = "klaus-moser"


def get_logger(name: str, log_file: str = None, backup_days: int = 7) -> logging.Logger:
    """
    Get a logger with the specified name and optional log file.

    :param name: Name of the logger.
    :param log_file: Path to the log file (optional).
    :param backup_days: Number of days to keep log files.
    :return: Configured logger.
    """

    logger = logging.getLogger(name)  # Create custom logger

    if not logger.hasHandlers():  # Avoid adding handlers if they are already added
        logger.setLevel(logging.INFO)

        fmt = '%(asctime)s | %(levelname)8s | %(message)s'  # Define format for logs

        # Create stdout handler for logging to the console (COLOR!)
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(level=logging.INFO)
        stdout_handler.setFormatter(fmt=CustomFormatter(fmt))
        logger.addHandler(hdlr=stdout_handler)  # Add handler

        if not log_file:
            logger.warning("No log file specified. Logging will be done only to the console.")
            return logger

        if not log_file.endswith(".log"):
            log_file = log_file.rstrip(".")  # Remove any trailing dots
            log_file = log_file + ".log"  # Ensure it ends with .log

        log_dir = Path(log_file).parent  # Get the directory from the log path

        if not log_dir.exists():  # Ensure the log directory exists
            log_dir.mkdir(parents=True, exist_ok=True)

        # Create a rotating file handler for logging to a file (NO COLOR!)
        file_handler = TimedRotatingFileHandler(
            filename=log_file,
            when='midnight',  # Rotate at midnight
            interval=1,  # Rotate every 1 day
            backupCount=backup_days  # Keep logs for the last X days
        )
        file_handler.suffix = "%Y_%m_%d.log"  # Custom suffix for rotated files
        file_handler.setLevel(level=logging.INFO)
        file_handler.setFormatter(fmt=logging.Formatter(fmt))
        logger.addHandler(hdlr=file_handler)  # Add handler

    return logger


if __name__ == '__main__':
    print(__file__)
