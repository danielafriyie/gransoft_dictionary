import logging
import os


class BaseLogger:
    """
    Base Logger class
    """

    def __init__(self, name=None, fmt=None):
        self._path = 'event_log'
        if not os.path.exists(self._path):
            os.mkdir(self._path)

        self.name = name if name else __name__
        self.fmt = fmt if fmt else '%(asctime)s:%(levelname)s:%(message)s'

        self._logger = logging.getLogger(name)
        self._logger.setLevel(level=logging.DEBUG)

        self._log_file_manager()

        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        file_handler = logging.FileHandler(f'{self._path}/event.log')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.ERROR)

        # stream_handler = logging.StreamHandler()
        # stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        # self._logger.addHandler(stream_handler)

    def _log_file_manager(self):
        """
        check if the log file in more than 10mb the it deletes it
        :return:
        """
        _path = f'{self._path}/event.log'

        if os.path.exists(_path):
            if os.path.getsize(_path) > 10485760:
                try:
                    os.remove(_path)
                except PermissionError as e:
                    self._logger.exception(e)

    def __call__(self):
        return self._logger


def logger(*args, **kwargs):
    _logger = BaseLogger(*args, **kwargs)
    return _logger()
