# --
# File name: IniManager.py
# --

from configparser import ConfigParser

class IniManager(object):

    '''
    ReadFileTEST: Read
    '''
    @staticmethod
    def ReadFile(fileFullpath) -> list():
        result = dict()
        iniconfig = ConfigParser()
        iniconfig.read(fileFullpath)

        # LOOPING
        # print(">> LOOPING : ")
        for currentSection0, currentSection1 in iniconfig.items():
            # print(f"{currentSection0}")
            # print(f"{currentSection1}")

            result[currentSection0] = dict()

            for currentSubsection0, currentSubsection1 in currentSection1.items():
                # print(f"{currentSubsection0}")
                # print(f"{currentSubsection1}")
                
                result[currentSection0][currentSubsection0] = currentSubsection1
            #
        #
        # print()
        return result
    #

    @staticmethod
    def WriteFile(fileFullpath):
        pass
    #
#
