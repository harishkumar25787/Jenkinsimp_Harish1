import traceback
import  os


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class webdriverfactory():

    def __init__(self,browser):
        self.browser = browser

    def webdriverinstanc(self):

        baseurl = "https://learn.letskodeit.com/p/practice"

        if self.browser == 'firefox':
            binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            caps = DesiredCapabilities().FIREFOX
            caps["marionette"] = True
            driver = webdriver.Firefox(capabilities=caps, firefox_binary=binary, executable_path="D:\\Pythondriver\\geckodriver.exe")
            driver.maximize_window()
            driver.implicitly_wait(3)
            driver.get(baseurl)
            print("Running on Firefox")
            return driver
        elif self.browser == 'chrome':
             driverLocation = "D:\\Pythondriver\\chromedriver.exe"
             os.environ["webdriver.chrome.driver"] = driverLocation
             driver = webdriver.Chrome(driverLocation)
             driver.maximize_window()
             driver.implicitly_wait(3)
             driver.get(baseurl)
             print("Running on Chrome")
             return  driver

        elif self.browser == 'IE':
            driverLocation = "D:\\Pythondriver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.implicitly_wait(3)
            driver.get(baseurl)
            print("Running on IE")
            return driver

        else:
            driverLocation = "D:\\Pythondriver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.implicitly_wait(3)
            driver.get(baseurl)
            print("Running on Chrome")
            return driver
            print("no browser is running ")
