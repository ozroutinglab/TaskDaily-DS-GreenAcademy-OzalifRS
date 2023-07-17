'''
File name : Config.py
Desc      : Config for development or production environment
'''

import os
from Helper.IniManager import IniManager


class Config(object):
    NAME = str()
    SUFFIX_DIR = "task\\Configurations"
    FILENAME = "global.ini"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "needs to be changed"
# endClass


class ProductionConfig(Config):
    NAME = "PRODUCTION"
    DEBUG = False
# endClass


class StagingConfig(Config):
    NAME = "STAGING"
    DEVELOPMENT = True
    DEBUG = True
# endClass


class DevelopmentConfig(Config):
    NAME = "DEVELOPMENT"
    DEVELOPMENT = True
    DEBUG = True
# endClass


class TestingConfig(Config):
    NAME = "TESTING"
    TESTING = True
# endClass


def GetConfig():
    fullpath = os.path.abspath(os.path.join(Config.SUFFIX_DIR, Config.FILENAME))
    config = IniManager.ReadFile(fullpath)
    # print(f">> fullpath:\n{fullpath}")
    # print(f">> config:\n{config}")
    if config['ENVIRONMENT']['option'] == StagingConfig.NAME:
        return StagingConfig
    if config['ENVIRONMENT']['option'] == DevelopmentConfig.NAME:
        return StagingConfig
    if config['ENVIRONMENT']['option'] == TestingConfig.NAME:
        return StagingConfig
    return ProductionConfig
#
