'''
File name: LoggingDS.py
'''

import logging
import Helper.Config as Config

LEVEL_INFO = logging.INFO
LEVEL_WARNING = logging.WARNING
LEVEL_DEBUG = logging.DEBUG
LEVEL_ERROR = logging.ERROR
LEVEL_CRITICAL = logging.CRITICAL


class LoggingDS(object):
    '''
    '''
    def __init__(self, logformat="%(asctime)s: %(message)s", level=LEVEL_INFO,
                 dateFormat="%H:%M:%S") -> None:
        self.SetConfig(logformat, level, dateFormat)
    #

    def SetConfig(self, logformat, level, dateFormat):
        self.format = logformat
        self.level = level  # By Default is INFO level. Other option NOTSET, WARNING, DEBUG, ERROR, WARN
        self.dateFormat = dateFormat

        logging.basicConfig(
            format=self.format,
            level=self.level,
            datefmt=self.dateFormat
        )
        if not Config.GetConfig().DEBUG:
            logging.disable(LEVEL_INFO)
    #

    def Show(self, message) -> None:
        if self.level is logging.INFO:
            self.ShowInfo(message)
        elif self.level is logging.WARNING:
            self.ShowWarning(message)
        elif self.level is logging.DEBUG:
            self.ShowDebug(message)
        elif self.level is logging.ERROR:
            self.ShowError(message)
        elif self.level is logging.CRITICAL:
            self.ShowCritical(message)
        #
    #

    def ShowInfo(self, message) -> None:
        # print(f">> logging.getLevelName: {logging.getLevelName}")
        # print(f">> self.level: {self.level}")
        logging.info(message)
    #

    def ShowWarning(self, message) -> None:
        logging.warning(message)
    #

    def ShowDebug(self, message) -> None:
        logging.debug(message)
    #

    def ShowError(self, message) -> None:
        logging.error(message)
    #

    def ShowCritical(self, message) -> None:
        logging.critical(message)
    #
#
