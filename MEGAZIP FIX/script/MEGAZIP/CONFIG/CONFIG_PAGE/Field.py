import pyodbc
import pandas as pd
import re
import time
import difflib
import importlib.util
from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from importlib.machinery import SourceFileLoader

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class Read_field(BasePage):
    def Read_field_by_id(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.ID,(idfield))).get_attribute('value')
        compr = (dtcomp == vfield)
        Cetak = (Jdlskenario, skenario, compr, dtcomp, vfield, datetime.today())
        writer.writerow(Cetak)
    
    def Read_field_is_required_by_xpath(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.XPATH, idfield)).get_attribute('required')
        compr = (dtcomp == vfield)
        Cetak = (Jdlskenario, skenario, compr, dtcomp, vfield, datetime.today())
        writer.writerow(Cetak)

    def Read_field_colour_by_id(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.ID,(idfield))).get_attribute('bgcolor')
        compr = (dtcomp == vfield)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, vfield, datetime.today())
        writer.writerow(Cetak)
        
class Text_Label(BasePage):
    def Text_Label_by_xpath(self,idfield,dtcomp,Jdlskenario, skenario,  Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.XPATH, idfield)).text
        compr = (dtcomp == vfield)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, vfield, datetime.today())
        writer.writerow(Cetak)

    def Text_Label_by_xpath_get_value_regex(self,idfield,dtcomp,Jdlskenario, skenario,  Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.XPATH, idfield)).get_attribute('value')
        label_td1 = re.search(dtcomp, vfield).group()
        compr = (dtcomp == label_td1)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, label_td1, datetime.today())
        writer.writerow(Cetak)
        
    def Text_Label_by_xpath_get_value(self,idfield,dtcomp,Jdlskenario, skenario,  Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.XPATH, idfield)).get_attribute('value')
        compr = (dtcomp == vfield)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, vfield, datetime.today())
        writer.writerow(Cetak)
        
    def Text_Label_by_id(self,idfield,dtcomp,Jdlskenario, skenario,  Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.ID,(idfield))).text
        compr = (dtcomp == vfield)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, vfield, datetime.today())
        writer.writerow(Cetak)
        
class Enable_field(BasePage):
    def Enable_field_by_id(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.ID,(idfield))).is_enabled()
        if(vfield == True):
            stat_field = 'Enabled'
        else:
            stat_field = 'Disabled'
        compr = (dtcomp == stat_field)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, stat_field, datetime.today())
        writer.writerow(Cetak)

    def Enable_field_by_xpath(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.XPATH, idfield)).is_enabled()
        if(vfield == True):
            stat_field = 'Enabled'
        else:
            stat_field = 'Disabled'
        compr = (dtcomp == stat_field)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, stat_field, datetime.today())
        writer.writerow(Cetak)
    
class Click_button(BasePage):
    def button_validation_by_id(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.ID,(idfield))).is_enabled()
        if(vfield == True):
            stat_field = 'Clickable'
        else:
            stat_field = 'Unclickable'
        compr = (dtcomp == stat_field)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, stat_field, datetime.today())
        writer.writerow(Cetak)

    def button_validation_by_xpath(self,idfield,dtcomp,Jdlskenario, skenario, Cetak, writer):
        vfield = WebDriverWait(self.driver,1).until(lambda driver: driver.find_element(By.XPATH, idfield)).is_enabled()
        if(vfield == True):
            stat_field = 'Clickable'
        else:
            stat_field = 'Unclickable'
        compr = (dtcomp == stat_field)
        Cetak = (Jdlskenario, skenario, compr,  dtcomp, stat_field, datetime.today())
        writer.writerow(Cetak)

class compare_value_with_db(BasePage):
    def comp_val_db(self,db_val,field_val,Jdlskenario,skenario,Cetak,writer):
        compr = (db_val == field_val)
        Cetak = (Jdlskenario,skenario,compr,db_val,field_val, datetime.today())
        writer.writerow(Cetak) 
        

class file_dowloaded_name(BasePage):
    def getDownLoadedFileName(waitTime,self):
        self.driver.execute_script("window.open()")
        WebDriverWait(self.driver,10).until(EC.new_window_is_opened)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get("about:downloads")

        endTime = time.time()+waitTime
        while True:
            try:
                fileName = self.driver.execute_script("return document.querySelector('#contentAreaDownloadsView .downloadMainArea .downloadContainer description:nth-of-type(1)').value")
                if fileName:
                    print(fileName)
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    return fileName
            except:
                pass

class Compare_data(BasePage):
    def Compare_data_DB(self,databaru,datalama,Jdlskenario, skenario, Cetak, writer):
        compr = (datalama == databaru)
        Cetak = (Jdlskenario, skenario, compr,  datalama, databaru, datetime.today())
        writer.writerow(Cetak)