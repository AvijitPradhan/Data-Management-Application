import os
from selenium import webdriver
from selenium.webdriver.chrome.options import options


def before_all(context):
  print("configuring local driver")

def configure_local_driver(context):
  options = webdriver.ChromeOptions()
  
def before_feature(context, feature):
  pass

def before_scenario(context, scenario):
  pass

def after_scenario(context, scenario):
  pass

def after_all(context):
  pass

