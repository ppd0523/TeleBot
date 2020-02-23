import logging
import os
from logging.handlers import TimedRotatingFileHandler

class Logger:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self, name, path, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter('%(asctime)s %(levelname)-7s %(lineno)3s:%(funcName)-15s %(message)s')
        # terminal logging
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def setLevel(self, level):
        self.logger.setLevel(level)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)


logger = Logger('TelegramBot', '')
