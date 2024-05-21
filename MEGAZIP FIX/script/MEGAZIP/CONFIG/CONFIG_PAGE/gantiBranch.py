from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from importlib.machinery import SourceFileLoader
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class ChangeBranch(BasePage):
    def Change(self):
        # UBAH BRANCH
        
        sleep(1)
        BRANCH = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('ddlBranchMaster'))
        BRANCH.click()
        print('novis')
        BRANCH = self.driver.find_element_by_xpath('//*[@id="ddlBranchMaster"]/option[2]')
        sleep(1)
        BRANCH.click()

# # UBAH BRANCH
# BRANCH = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_id('ddlBranchMaster'))
# BRANCH.click()
# BRANCH = driver.find_element_by_xpath('//*[@id="ddlBranchMaster"]/option[2]')
# sleep(1)
# BRANCH.click()       