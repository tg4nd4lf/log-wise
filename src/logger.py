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

import os
import logging
import datetime
from .formatter import CustomFormatter

__version__ = "1.0"
__author__ = "klaus-moser"


def configure_logger(filename: str = None) -> logging.Logger:
    """
    Set up logger.

    :return: Logger instance.
    """

    # Create custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Define format for logs
    fmt = '%(asctime)s | %(levelname)8s | %(message)s'

    # Create stdout handler for logging to the console
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(CustomFormatter(fmt))

    # Create file handler for logging to a file
    today = datetime.date.today()

    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), '{}_{}.log'.format("my_app_", today.strftime('%Y_%m_%d')))
    else:
        filename = '{}_{}.log'.format(filename, today.strftime('%Y_%m_%d'))

    file_handler = logging.FileHandler(filename=filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(fmt))

    # Add both handlers to the logger
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    print(__file__)
