import unittest
import pyodbc
import difflib
import page
import random
import string
import csv
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

    def POBEPage1(self,vara):
        # Nama Lengkap
        namaLengkap = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('CustCustomerData_cust_complete_name'))
        namaLengkap.click()
        sleep(1)
        namaLengkap.send_keys(vara.array["NamaLengkap"])
        namaLengkap.click()
        sleep(1)   

        # Nama Panggilan
        namaPanggilan = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('CustCustomerData_cust_call_name'))
        namaPanggilan.click()
        sleep(1)
        namaPanggilan.send_keys('ANANDA CITRA ISLAMI')
        namaPanggilan.click()
        sleep(1)   

        # Masa Berlaku KTP
        berlakuKTP = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('berlakuKTP'))
        berlakuKTP.click()
        sleep(1)
        berlakuKTP.send_keys('31/12/2022')
        berlakuKTP.click()
        sleep(1)   

        # Alamat KTP
        alamatKTP = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('CustCustomerData_card_address'))
        alamatKTP.click()
        sleep(1)
        alamatKTP.send_keys('Jln Rumah')
        alamatKTP.click()
        sleep(1)

        # RT
        RT = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('CustCustomerData_card_rt'))
        RT.click()
        sleep(1)
        RT.send_keys('000')
        RT.click()
        sleep(1)

        # RW
        RW = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element_by_id('CustCustomerData_card_rw'))
        RW.click()
        sleep(1)
        RW.send_keys('000')
        RW.click()
        sleep(1)


        
    

        