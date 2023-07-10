# File name : Sesi4_task_01.py
# Author    : Ozalif R.S.
# Desc      : Sesi 4 Practice 1

import os
from Engine import Sesi04TrafficLight
from Helper.LoggingDS import LoggingDS, LEVEL_INFO
from Helper.Stopwatch import Stopwatch

LOGGINGMAIN = LoggingDS(level=LEVEL_INFO)
LOGGINGMAIN.ShowInfo("** Sesi4_task_01 **")

if __name__ == "__main__":
    LOGGINGMAIN.ShowInfo(">> TEST START")

    trafficLightOne = Sesi04TrafficLight.TrafficLight("TL-01")
    trafficLightTwo = Sesi04TrafficLight.TrafficLight("TL-02")
    swatch = Stopwatch()
    maxTimeGreenlight = Sesi04TrafficLight.MAXTIME_GREEN
    maxTimeYellowlight = Sesi04TrafficLight.MAXTIME_YELLOW

    i = 0
    try:
        trafficLightOne.Start()
        trafficLightTwo.Stop()
        while True:
            i += 1
            print("******       WELCOME      ******")
            print("****** TRAFFIC CONTROLLER ******")
            print(i)
            currentGreenTimer = int(0)
            print(f">> currentTimer: {currentGreenTimer} s")

            trafficLightOne.ShowTrafficStatus()
            trafficLightTwo.ShowTrafficStatus()
            LOGGINGMAIN.ShowInfo(" --------------- ")
            swatch.Start()
            while currentGreenTimer <= maxTimeGreenlight:
                if currentGreenTimer % 1 == 0:
                    LOGGINGMAIN.ShowInfo(f"currentGreenTimer: {currentGreenTimer} s")
                    trafficLightOne.ShowTrafficStatus()
                    trafficLightTwo.ShowTrafficStatus()
                    LOGGINGMAIN.ShowInfo(" --------------- ")
                currentGreenTimer = swatch.GetTimeSecond()
            #
            trafficLightOne.ShowTrafficStatus()
            trafficLightTwo.ShowTrafficStatus()
            LOGGINGMAIN.ShowInfo(" --------------- ")

            currentYellowTimer = int(0)
            if trafficLightOne.currentActiveLight == Sesi04TrafficLight.LightColor.GREEN:
                trafficLightOne.PrepareTostop()
                swatch.Reset()
                swatch.Start()
                while currentYellowTimer <= maxTimeYellowlight:
                    if currentYellowTimer % 1 == 0:
                        trafficLightOne.ShowTrafficStatus()
                        trafficLightTwo.ShowTrafficStatus()
                        LOGGINGMAIN.ShowInfo(" --------------- ")
                    currentYellowTimer = swatch.GetTimeSecond()
                #
                trafficLightOne.Stop()
                trafficLightTwo.Start()
                trafficLightOne.ShowTrafficStatus()
                trafficLightTwo.ShowTrafficStatus()
                LOGGINGMAIN.ShowInfo(" --------------- ")
            else:
                trafficLightTwo.PrepareTostop()
                swatch.Reset()
                swatch.Start()
                while currentYellowTimer <= maxTimeYellowlight:
                    if currentYellowTimer % 1 == 0:
                        trafficLightOne.ShowTrafficStatus()
                        trafficLightTwo.ShowTrafficStatus()
                        LOGGINGMAIN.ShowInfo(" --------------- ")
                    currentYellowTimer = swatch.GetTimeSecond()
                #
                trafficLightOne.Start()
                trafficLightTwo.Stop()
                trafficLightOne.ShowTrafficStatus()
                trafficLightTwo.ShowTrafficStatus()
                LOGGINGMAIN.ShowInfo(" --------------- ")
            #
            import time
            time.sleep(5)
            os.system('cmd /c cls')
    except KeyboardInterrupt:
        pass
    #

    LOGGINGMAIN.ShowInfo(">> TEST END")
# endMain
LOGGINGMAIN.ShowInfo("** Sesi4_task_01 **")
