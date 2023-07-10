'''
File name : Stopwatch.py
Desc      : Stopwatch based on time module
'''

import time
from Helper.LoggingDS import LoggingDS, LEVEL_INFO


class Stopwatch(object):
    def __init__(self) -> None:
        super().__init__()
        self.__swatchLog = LoggingDS(level=LEVEL_INFO)
        self.__startTime = int()
        # self.__lapTime = int()
    #

    def Reset(self) -> None:
        self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-Reset")
        self.__startTime = int()
        # self.__lapTime = int()
    #

    def Start(self) -> None:
        self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-Start")
        # self.startTime = time.time()
        self.__startTime = time.perf_counter_ns()
        self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-Starting time: {self.__startTime}")
    #

    def GetTimeNanosecond(self) -> float:
        self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-GetTimeNanosecond")
        # return time.time() - self.startTime
        return time.perf_counter_ns() - self.__startTime
    #

    def GetTimeMicrosecond(self) -> float:
        self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-GetTimeMicrosecond")
        # return time.time() - self.startTime
        duration = time.perf_counter_ns() - self.__startTime
        return duration / 1000
    #

    def GetTimeMilisecond(self) -> float:
        self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-GetTimeMilisecond")
        # return time.time() - self.startTime
        duration = time.perf_counter_ns() - self.__startTime
        return duration / 1000000
    #

    def GetTimeSecond(self) -> float:
        # self.__swatchLog.ShowInfo(f"{self.__class__.__name__}-GetTimeSecond")
        # return time.time() - self.startTime
        duration = time.perf_counter_ns() - self.__startTime
        return duration / 1000000000
    #
#
