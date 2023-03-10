
import os
import odbc
import requests

def before_all(context):
  print("Set Validations or Bearer token for the required environment")

  
def before_feature(context, feature):
  pass
  *** Check for Test Data(Uri, Body parameters) from Swagger ***

def before_scenario(context, scenario):
  pass
*** CHeck for the Environment settings for a particular environment ***

def after_scenario(context, scenario):
  pass
*** Check in Database for validations after requests are sent ***

def after_all(context):
  pass

response = requests.request(​"DELETE"​, url, ​headers​=headers, ​verify​=​False​)

*** This will delete the created data ***
