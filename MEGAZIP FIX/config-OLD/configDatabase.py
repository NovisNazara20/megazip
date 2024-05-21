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
global serverMflos 
global databaseMflos
global usernameMflos 
global passwordMflos
# ----
global serverMzip 
global databaseMzip
global usernameMzip 
global passwordMzip
# ----
global serverPmf 
global databasePmf
global usernamePmf 
global passwordPmf
# ----
driver = "{SQL Server}"
serverMflos = "192.168.20.120"
databaseMflos = "MFLOS"
usernameMflos = "pmf_kurnia" 
passwordMflos = "123456789" 
# ----
driver = "{SQL Server}"
serverMzip = "192.168.20.60"
databaseMzip = "megazip"
usernameMzip = "pmf_kurnia" 
passwordMzip = "kurnia123" 
# ----
driver = "{SQL Server}"
serverPmf = "192.168.20.53"
databasePmf = "PMF"
usernamePmf = "pmf_kurnia" 
passwordPmf = "kurnia123" 

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        f = open("ReportDB.txt", "a")
        f.write("Internet Access \n")
        f.close()
        return True
    except:
        f = open("ReportDB.txt", "a")
        f.write("No Internet Access \n")
        f.close()
        return False
        
# test
print( "connected" if connect() else "no internet!" )


def DbMflos(query):
    try :
        conn = pyodbc.connect("DRIVER=" + driver
        + ";SERVER=" + serverMflos 
        + ";DATABASE=" + databaseMflos 
        + ";UID=" + usernameMflos  
        + ";PWD=" + passwordMflos )
        # print("Berhasil konek")
        cursor1 = conn.cursor()
        f = open("ReportDB.txt", "a")
        f.write("Connected successfully Database",serverMflos)
        f.close()
        # for row in cursor1.execute(query):
        return cursor1.execute(query)
        #     print(row)
    except:
        f = open("ReportDB.txt", "a")
        f.write("Error! Database connection Failed \n")
        f.close()
            
def DbMzip(query):
    try :
        conn = pyodbc.connect("DRIVER=" + driver
        + ";SERVER=" + serverMzip 
        + ";DATABASE=" + databaseMzip 
        + ";UID=" + usernameMzip  
        + ";PWD=" + passwordMzip )
        # print("Berhasil konek")
        cursor1 = conn.cursor()
        f = open("ReportDB.txt", "a")
        f.write("Connected successfully Database Megazip! \n")
        f.close()
        # for row in cursor1.execute(query):
        return cursor1.execute(query)
        #     print(row)
    except:
        f = open("ReportDB.txt", "a")
        f.write("Error! Database connection Failed \n")
        f.close()

def DbPmf(query):
    try :
        conn = pyodbc.connect("DRIVER=" + driver
        + ";SERVER=" + serverPmf 
        + ";DATABASE=" + databasePmf 
        + ";UID=" + usernamePmf  
        + ";PWD=" + passwordPmf )
        # print("Berhasil konek")
        cursor1 = conn.cursor()
        f = open("ReportDB.txt", "a")
        f.write("Connected successfully Database MFLOS! \n")
        f.close()
        # for row in cursor1.execute(query):
        return cursor1.execute(query)
        #     print(row)
    except:
        f = open("ReportDB.txt", "a")
        f.write("Error! Database connection Failed \n")
        f.close()
            