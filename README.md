# log-wise

Drop-in coloured logger with daily file rotation for any Python project.

## Install

```bash
# From the repo (editable, for local development)
pip install -e .

# Or directly from GitHub
pip install git+https://github.com/klaus-moser/log-wise.git
```

## Usage

```python
from log_wise import get_logger

# Console only
log = get_logger(__name__)

# Console + daily rotated log file
log = get_logger(__name__, log_file="logs/app")

log.debug("debug message")
log.info("info message")
log.warning("warning message")
log.error("error message")
log.critical("critical message")
```

### Parameters

| Parameter      | Default                                          | Description                          |
| -------------- | ------------------------------------------------ | ------------------------------------ |
| `name`         | —                                                | Logger name (typically `__name__`)   |
| `level`        | `logging.INFO`                                   | Minimum log level                    |
| `log_file`     | `None`                                           | Path to log file (`.log` auto-added) |
| `backup_days`  | `7`                                              | Days to keep rotated files           |
| `fmt`          | `%(asctime)s \| %(levelname)8s \| %(message)s`   | Log format string                    |

## License

[MIT](https://choosealicense.com/licenses/mit/)
