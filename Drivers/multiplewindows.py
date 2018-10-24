import time
import  unittest


from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
import os
class twowindows(unittest.TestCase):

    def test_broswer_window(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("http://toolsqa.com/handling-alerts-using-selenium-webdriver/")
        driver.find_element_by_xpath("//*[@id='content']/p[4]/button").click()
        ale = driver.switch_to.alert()
        print(ale.text)
        time.sleep(4)
        ale.accept()

        driver.find_element_by_xpath("//*[@id='content']/p[11]/button").click()
        popnale = driver.switch_to.alert()
        time.sleep(4)
        popnale.send_keys("harish")
        time.sleep(2)
        print(popnale.text)
        time.sleep(4)
        popnale.accept()
        driver.implicitly_wait(5)

        driver.find_element_by_xpath("//*[@id='content']/p[8]/button").click()
        conale = driver.switch_to.alert
        print(conale.text)
        time.sleep(4)

        conale.accept()


        # parentguid = driver.current_window_handle
        # print("currentwindow" +  " is   " + parentguid)
        # driver.find_element_by_id("two-window").click();
        # allGUID = driver.window_handles;
        #print("Page title before Switching : " + driver.getTitle);
