import logging
from logging.handlers import RotatingFileHandler
import os


class BaseLogger:
    """
    Base Logger class
    """

    def __init__(self, name=None, fmt=None):
        _path = 'event_log'
        if not os.path.exists(_path):
            os.mkdir(_path)

        self.name = name if name else __name__
        self.fmt = fmt if fmt else '%(asctime)s:%(levelname)s:%(message)s'

        self._logger = logging.getLogger(name)
        self._logger.setLevel(level=logging.DEBUG)

        formatter = logging.Formatter(self.fmt)
        file_handler = RotatingFileHandler(filename=f'{_path}/event.log', maxBytes=1024, backupCount=5)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.ERROR)

        # stream_handler = logging.StreamHandler()
        # stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        # self._logger.addHandler(stream_handler)

    def __call__(self):
        return self._logger


def logger():
    _logger = BaseLogger()
    return _logger()
