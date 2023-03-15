import os
from selenium import webdriver
from selenium.webdriver.chrome.options import options
from common.vtf_counter import VTFCounter


def before_all(context):
  print("configuring local driver")
  configure_local_driver(context)
  

def configure_local_driver(context):
  cwd = os.getcwd()
  options = webdriver.ChromeOptions()
  
def before_feature(context, feature):
  U.df = U.read_excel('//users/test/sheets', testcases)

def before_scenario(context, scenario):
  driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
  driver.maximize_window()
 
def after_scenario(context, scenario):
  driver.execute_script("window.scrollBy(0,0)","")
  

def after_all(context):
  driver.close_window()
  
  

