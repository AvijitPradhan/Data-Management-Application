import os
from selenium import webdriver
from selenium.webdriver.chrome.options import options


@before_all(context):
  print("configuring local driver")

def configure_local_driver(context):
  options = webdriver.ChromeOptions()
  
@before_feature(context, feature):
  U.df = U.read_excel('//sheet_location', sheetname)

@before_scenario(context, scenario):
  def someFunc(scenario):
  Log.Message("Before running the " + scenario.Name + "scenario")
  

@after_scenario(context, scenario):
  def someFunc(scenario):
  Log.Message("The " + scenario.Name + " scenario has been executed")

@after_all(context):
  def someFunc(param1):
  global dbConnection
  dbConnection.Close()

