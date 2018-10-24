from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import Utility.logger as cl
import logging
import os
import time

class seleniumdrivers():

    log = cl.customlogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def screenshot(self,resultmessage):

        filename =  resultmessage + "." + str(round(time.time())*1000) + ".png"
        screenshotdirectory = "..//Screenshots/"
        relativefilename  = screenshotdirectory + filename
        currentdirectory = os.path.dirname(__file__)
        destinationfile = os.path.join(currentdirectory,relativefilename)
        destionationdirectory  = os.path.join(screenshotdirectory,currentdirectory)

        try :

            if not os.path.exists(destionationdirectory):
                os.makedirs(destionationdirectory)
            self.driver.save_screenshot(destinationfile)
            self.log.info("screenshot save to directory" + destinationfile)

        except:
            self.log.info("exception occured while taking screeenshot")
            print_stack()


    def gettitle(self):
        return self.driver.title


    def getbytype(self, locatortype):

        locatortype = locatortype.lower()


        if locatortype == "id":
            return By.ID

        elif locatortype == "name":
            return By.NAME

        elif locatortype == "xpath":
            return By.XPATH

        elif locatortype == "css":
            return By.CSS_SELECTOR

        elif locatortype == "class":
            return By.CLASS_NAME

        elif locatortype == "link":
            return By.LINK_TEXT

        elif locatortype == "partial_linktext":
            return By.PARTIAL_LINKTEXT

        elif locatortype == "tagname":
            return By.TAG_NAME

        else :
            self.log.info("Locator type " + locatortype + "not supported ")

