"""log-wise — a drop-in coloured logger for any Python project."""

from .formatter import ColorFormatter
from .logger import get_logger

__all__ = ["get_logger", "ColorFormatter"]
__version__ = "3.0.0"
