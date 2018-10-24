import time
import  unittest
from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class test_broswer(unittest.TestCase):

    def test_broswer_window(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://chercher.tech/python/switchto")
        parentGUID = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id = 'two-window']").click()
        time.sleep(3)
        allguid = driver.window_handles
        print("Page title before switching : " + str(driver.title()))
        print("Total windows : " + allguid.size())

        for guid in allguid:
            if(guid!= parentGUID):
                driver.switch_to.window(guid)

                break

        google = driver.find_elements_by_name("g")
        google.send_keys('success')
        print("page title after swithcing to google : " + driver.title())
        driver.switch_to.window(parentGUID)
        print("Page title after switching back to Parent: " + driver.title());