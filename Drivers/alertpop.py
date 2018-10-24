import time
import  unittest


from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
import os


class alertpop(unittest.TestCase):


    def test_simplealert(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("file:///C:/Users/hsholapur/Desktop/simple.html")

        button = driver.find_element_by_xpath("//*[@name = 'alert']")
        button.click()
        time.sleep(2)
        obj = driver.switch_to.alert
        mess = obj.text
        print( "simple alert is " + mess)
        obj.accept()
        driver.quit()


    def test_cofirm(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("file:///C:/Users/hsholapur/Desktop/confirm.html")
        button1 = driver.find_element_by_name("alert")
        button1.click()
        time.sleep(2)
        obj2 = driver.switch_to.alert
        mess1 = obj2.text
        print ("cofirmation message is " + mess1)
        obj2.accept()
        text1 = driver.find_element_by_id("msg")
        print(text1.text)
        time.sleep(3)
        driver.refresh()
        button1 = driver.find_element_by_name("alert")
        button1.click()
        obj3 = driver.switch_to.alert
        obj3.dismiss()
        text2 = driver.find_element_by_id("msg")
        print(text2.text)
        driver.quit()
    def test_prompt(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("file:///C:/Users/hsholapur/Desktop/prompt.html")
        button1 = driver.find_element_by_name("employeeLogin")
        button1.click()
        prompt = driver.switch_to.alert
        time.sleep(4)
        prompt.send_keys("Harishkumar what is happen to aleet pop")
        time.sleep(4)
        prompt.accept()
        time.sleep(4)
        prompt.accept()
        text4 = driver.find_element_by_id("msg")
        print(text4.text)











