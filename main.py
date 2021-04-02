# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from seleniumUtil.webnevigate import webNevigation
import time
import sys
# import settings
# from seleniumUtil.chromdriver import drivers
import json
from dbUtil.get_data import getLink




class StartBot:
    def __init__(self):
        self.start()

    def start(self):
        data = getLink.link()
        webNevigation.DataSegregation(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    StartBot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
