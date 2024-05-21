from msilib.schema import Class
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

# class var_login_pak_kur(BasePage):
#     array = {}
#     array['array_login_main_username'] = '201902288'
#     array['array_pass_main_username'] =  'Wijaya1!'
    
# class var_login_ferdinand(BasePage):
#     array = {}
#     array['array_login_main_username'] = '202201969'
#     array['array_pass_main_username'] =  'Wijaya1!'
    
# class var_login_mariam(BasePage):
#     array = {}
#     array['array_login_main_username'] = '201902288'
#     array['array_pass_main_username'] =  'Wijaya1!'
    
class var_login_novis(BasePage):
    array = {}
    array['array_login_main_username'] = '202100317'
    array['array_pass_main_username'] =  '123456'

# class var_login_radit(BasePage):
#     array = {}
#     array['array_login_main_username'] = '201902288'
#     array['array_pass_main_username'] =  'Wijaya1!'