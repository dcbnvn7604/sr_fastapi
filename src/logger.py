import logging
from contextvars import ContextVar
from logging import LogRecord


request_id = ContextVar('request_id')

class ContextFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        record.request_id = request_id.get()
        return True


logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(request_id)s - %(message)s')

ch.setFormatter(formatter)
ch.addFilter(ContextFilter())

logger.addHandler(ch)
