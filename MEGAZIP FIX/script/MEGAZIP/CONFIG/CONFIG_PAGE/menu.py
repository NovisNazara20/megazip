import unittest
import random
import string
#
from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from importlib.machinery import SourceFileLoader

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class MainPage(BasePage): 
    def menuOE(self):        
        element1 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/a') #loan
        element2 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[7]') #Sales
        element3 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[7]/ul/li[1]') #OrderEntry
        sleep(1)
        hoverover =ActionChains(self.driver).move_to_element(element1).move_to_element(element2).move_to_element(element3).click().perform()
        self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul').click()
        sleep(1)

    def menuSurvey(self):        
        element1 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/a') #loan
        element2 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[1]/a') #Admin Kredit
        element3 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[1]/ul/li[1]/a') #Additional Entry
        element4 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[1]/ul/li[4]/a') #Survey Entry
        sleep(1)
        hoverover =ActionChains(self.driver).move_to_element(element1).click().move_to_element(element2).click().move_to_element(element3).click().move_to_element(element4).click().perform()
        self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul').click()
        sleep(1)

    def menuAdditonal(self): 
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(self.driver.find_element_by_xpath('//*[@id="topnav"]/div[1]')))
        # element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navigation"]/div/div[2]/ul/li[2]')))
        # sleep(1)
        element1 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/a') #loan
        element2 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[1]/a') #Admin Kredit
        element3 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul/li[2]/ul/li[1]/ul/li[1]/a') #Additional Entry
        sleep(1)

        hoverover =ActionChains(self.driver).move_to_element(element1).click().click().move_to_element(element2).click().move_to_element(element3).click().perform()
        self.driver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/ul').click()
        sleep(1)

    def Random(self):
        digitsNoAppl = ''.join(random.sample(string.digits, 7))
        digitsNoka = ''.join(random.sample(string.digits, 6))
        digitsNosin = ''.join(random.sample(string.digits, 6))
        digitsNopol = ''.join(random.sample(string.digits, 2))
        digitsBPKP = ''.join(random.sample(string.digits, 3))
        charsNoka = ''.join(random.sample(string.ascii_letters, 8))
        charsNosin = ''.join(random.sample(string.ascii_letters, 8))
        charsNopol = ''.join(random.sample(string.ascii_letters, 2))
        charsBPKP = ''.join(random.sample(string.ascii_letters, 3))


