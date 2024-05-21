from time import sleep
from importlib.machinery import SourceFileLoader
from selenium import webdriver

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class MainPage(BasePage):
    def username(self,array):
        mainPage = SourceFileLoader("locator","script/MEGAZIP/CONFIG/CONFIG_PAGE/locator.py").load_module() 
        mainPage = mainPage.BasePageElementUsername()
        mainPage = self.driver.find_element(*mainPage.USERNAME)
        mainPage.click()
        mainPage.send_keys(array.array["array_login_main_username"])
        mainPage.click()

    def password(self,array):
        mainPage = SourceFileLoader("locator","script/MEGAZIP/CONFIG/CONFIG_PAGE/locator.py").load_module() 
        mainPage = mainPage.BasePageElementPass()
        mainPage = self.driver.find_element(*mainPage.PASSWORD)
        mainPage.click()
        mainPage.send_keys(array.array["array_pass_main_username"])
        mainPage.click()

    def click_go_button(self):
        mainPage = SourceFileLoader("locator","script/MEGAZIP/CONFIG/CONFIG_PAGE/locator.py").load_module() 
        mainPage = mainPage.MainPageLocator()
        try:
            element = self.driver.find_element(*mainPage.GO_BUTTON)
            element.click()
            f = open("ReportExPage.txt", "a")
            f.write("Submit : Passed! \n")
            f.close()
        except:
            fa = open("ReportExPage.txt", "a")
            fa.write("Submit : Failed! \n")
            fa.close()
    