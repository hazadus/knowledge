📁 [[Libraries]]

-----
## References
- [Documentation](https://www.structlog.org/en/stable/getting-started.html)
- [Logging Best Practices](https://www.structlog.org/en/stable/logging-best-practices.html)
- [A Comprehensive Guide to Python Logging with Structlog](https://betterstack.com/community/guides/logging/structlog/)

----
## Examples
- [Demo Configuration of logger](https://github.com/hazadus/verify-social/blob/main/bot-ig/src/logger.py)

```python
# logger.py
import os
from pathlib import Path

import structlog

if os.getenv("DEBUG"):
    # Log to console in DEBUG mode, in human-readable form
    logger_factory = None
    output_processor = structlog.dev.ConsoleRenderer()
else:
    # Otherwise, log JSON records to file
    if not os.path.exists("logs"):
        os.mkdir("logs")
    logger_factory = structlog.WriteLoggerFactory(
        file=(Path("logs") / Path("bot-ig")).with_suffix(".log").open("a"),
    )
    output_processor = structlog.processors.JSONRenderer()

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.dict_tracebacks,
        structlog.processors.EventRenamer("msg"),
        output_processor,
    ],
    logger_factory=logger_factory,
)
logger = structlog.get_logger()
```