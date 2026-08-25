"""ANSI color formatter for console log output."""

from __future__ import annotations

import logging

_COLORS: dict[int, str] = {
    logging.DEBUG: "\x1b[38;5;39m",      # blue
    logging.INFO: "\x1b[38;5;250m",      # grey
    logging.WARNING: "\x1b[38;5;226m",   # yellow
    logging.ERROR: "\x1b[38;5;196m",     # red
    logging.CRITICAL: "\x1b[31;1m",      # bold red
}
_RESET = "\x1b[0m"


class ColorFormatter(logging.Formatter):
    """Wrap each log line in ANSI color codes based on severity.

    Adapted from https://stackoverflow.com/a/56944256/3638629
    """

    def __init__(self, fmt: str | None = None, datefmt: str | None = None) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt)
        self._formatters: dict[int, logging.Formatter] = {
            level: logging.Formatter(f"{color}{fmt}{_RESET}", datefmt=datefmt)
            for level, color in _COLORS.items()
        }

    def format(self, record: logging.LogRecord) -> str:  # noqa: A003
        formatter = self._formatters.get(record.levelno, self._formatters[logging.INFO])
        return formatter.format(record)
