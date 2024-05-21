import pyodbc
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver
        
        
global driver
global server 
global database 
global username 
global password
driver = "{SQL Server}"
server = "192.168.20.53"
database = "pmf"
username = "pmf_kurnia" 
password = "kurnia123"

def DbPMF(query):
    try :
        conn = pyodbc.connect("DRIVER=" + driver
        + ";SERVER=" + server 
        + ";DATABASE=" + database 
        + ";UID=" + username  
        + ";PWD=" + password )
        # print("Berhasil konek")
        cursor1 = conn.cursor()
        f = open("ReportDB.txt", "a")
        f.write("Connect to DB PMF! \n")
        f.close()
        # for row in cursor1.execute(query):
        return cursor1.execute(query)
        #     print(row)
    except:
        f = open("ReportDB.txt", "a")
        f.write("Tidak dapat Konek ke DB PMF! \n")
        f.close()
        