import logging
import json
from datetime import datetime


class JSONFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
    def format(self, record):
        return json.dumps({
            "level": record.levelname,
            "timestamp": datetime.now().isoformat(),
            "message": super().format(record)
        })


def setup_logging():
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logging.root.handlers = [handler]
