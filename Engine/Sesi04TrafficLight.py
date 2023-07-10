'''
File name: Sesi04TrafficLight.py
'''

from Helper.LoggingDS import LoggingDS, LEVEL_INFO
from enum import Enum

MAXTIME_GREEN = 30
MAXTIME_YELLOW = 15


class LightColor(Enum):
    RED = 1  
    YELLOW = 2
    GREEN = 3
    BLACK = 4
#


class TrafficLight(object):

    def __init__(self, name) -> None:
        self.currentActiveLight = LightColor.BLACK
        self.timeDelay = 1  # 1 sec
        self.maxTime = 30
        self.name = name
        self.__trafficLog = LoggingDS(level=LEVEL_INFO)
    #

    def Start(self):
        self.__trafficLog.ShowInfo(f"{self.__class__.__name__}-Start")
        self.currentActiveLight = LightColor.GREEN
    #

    def PrepareTostop(self):
        self.__trafficLog.ShowInfo(f"{self.__class__.__name__}-PrepareTostop")
        self.currentActiveLight = LightColor.YELLOW
    #

    def Stop(self):
        self.__trafficLog.ShowInfo(f"{self.__class__.__name__}-Stop")
        self.currentActiveLight = LightColor.RED
    #

    def ShowTrafficStatus(self):
        self.__trafficLog.ShowInfo(f"Traffic light {self.name}: {self.currentActiveLight.name}")
    #
#
