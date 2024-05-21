import pyodbc
import pandas as pd
import urllib.request
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
server = "192.168.20.120"
database = "MFLOS"
username = "pmf_kurnia" 
password = "123456789" 

def DbMflos(query):
    try :
        conn = pyodbc.connect("DRIVER=" + driver
        + ";SERVER=" + server 
        + ";DATABASE=" + database 
        + ";UID=" + username  
        + ";PWD=" + password )
        # print("Berhasil konek")
        cursor1 = conn.cursor()
        f = open("ReportDB.txt", "a")
        f.write("Connect to DB MFLOS! \n")
        f.close()
        # for row in cursor1.execute(query):
        return cursor1.execute(query)
        cursor1.commit()
        #     print(row)
    except:
        f = open("ReportDB.txt", "a")
        f.write("Tidak dapat Konek ke DB MFLOS! \n")
        f.close()


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        f = open("ReportDB.txt", "a")
        f.write("Connect Internet \n")
        f.close()
        return True
    except:
        f = open("ReportDB.txt", "a")
        f.write("Tidak dapat Konek ke DB MFLOS! \n")
        f.close()
        return False
# test
print( "connected" if connect() else "no internet!" )


            