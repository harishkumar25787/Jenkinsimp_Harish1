import time
import  unittest
import xlrd
import sys
import win32com.client
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import os
from ddt import ddt,data,unpack
from Drivers.exceldata import getexceldata
@ddt
class test_data(unittest.TestCase):

    @data(*getexceldata("D:\\loginpages.xlsx"))
    @unpack
    def test_datadriven(self, username, key1):

        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        self.driver = webdriver.Chrome(driverlocation)
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://learn.letskodeit.com/")
        print(self.driver.title)
        LOGID = self.driver.find_element_by_link_text("Login").click()
        time.sleep(3)

        i = 3
        while(i<3):
            emailid = self.driver.find_element_by_id("user_email")
            password = self.driver.find_element_by_id("user_password")
            emailid.clear()
            emailid.send_keys(username)
            password.clear()
            password.send_keys(key1)
            time.sleep(2)
            self.driver.find_element_by_name("commit").click()
            i=i+1

