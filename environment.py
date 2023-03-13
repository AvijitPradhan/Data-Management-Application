
import os
import pyodbc
import requests

def before_all(context):
  print("Set Validations or Bearer token for the required environment")

  
def before_feature(context, feature):
  *** To get the cookies ***
  
  x = requests.post(url, data=data) 
  print x.cookies
 

def before_scenario(context, scenario):
  pass
*** CHeck for API KEY and Bearer token for the particular API ***


def after_scenario(context, scenario):
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL};User ID=myuserid;Password=mypassword;Server=myserver;Database=mydatabase;Port=myport;String Types=Unicode')


def after_all(context):

response = requests.request(​"DELETE"​, url, ​headers​=headers, ​verify​=​False​)

*** This will delete the created data ***
