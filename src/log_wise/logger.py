"""Factory function that creates a pre-configured logger."""

from __future__ import annotations

import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from .formatter import ColorFormatter

_DEFAULT_FMT = "%(asctime)s | %(levelname)8s | %(message)s"


def get_logger(
    name: str,
    *,
    level: int = logging.INFO,
    log_file: str | Path | None = None,
    backup_days: int = 7,
    fmt: str = _DEFAULT_FMT,
) -> logging.Logger:
    """Return a named logger with colored console output and optional file rotation.

    Parameters
    ----------
    name:
        Logger name (typically ``__name__``).
    level:
        Minimum log level (default ``INFO``).
    log_file:
        Optional path to a log file.  ``.log`` is appended when no suffix is
        given.  The parent directory is created automatically.
    backup_days:
        How many daily rotated log files to keep (default 7).
    fmt:
        Log format string.

    Returns
    -------
    logging.Logger
        A ready-to-use logger instance.
    """
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(level)

    # Console handler (colored)
    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(ColorFormatter(fmt))
    logger.addHandler(console)

    if log_file is None:
        return logger

    # File handler (plain text, daily rotation)
    log_path = Path(log_file)
    if not log_path.suffix:
        log_path = log_path.with_suffix(".log")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    file_handler = TimedRotatingFileHandler(
        filename=log_path,
        when="midnight",
        interval=1,
        backupCount=backup_days,
    )
    file_handler.suffix = "%Y-%m-%d"
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(file_handler)

    return logger
