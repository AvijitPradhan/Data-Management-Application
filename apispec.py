
from behave import *
import requests
import pyodbc

@given("User has all the prerequisites for POST and GET requests")
  def step_impl(context):
    GETurl = "/api/users/2"
    POSTurl = "/api/users/"
    payload = "{\"user\":{{"name": "morpheus","job": "leader"}}"
    headers = {'accept': “application/json”}

@when ("User sends POST requests")
  def step_impl(context, status_code):
   
   url = "/api/users/"
   payload = "{\"user\":{{"name": "morpheus","job": "leader"}}"
   headers = {'accept': “application/json”}
   response = requests.request("POST", url, data=payload, headers=headers, verify=False)
   print(response.text)
   
   actual_status_code = response.status_code
   assert actual_status_code == int(status_code)
   
 @then ("User should be created")
   def step_impl(context):
    cnxn = pyodbc.connect("DSN=REQRES")
    cursor = cnxn.cursor()
    cursor.tables()
    rows = cursor.fetchall()
    
    for row in table:
            first_name = row['First_name']
            last_name = row['Last_name']
            email = row['Mail-id']
            return first_name, last_name, email
    assert first_name == payload.name
    
@then ("User sends GET request")
  def step_impl(context):
   url = "/api/users/2"
   headers = {'accept': “application/json”}
   response = requests.request("GET", url,params=querystring, headers=headers, verify=False)
   print(response.text)
   
   actual_status_code = response.status_code
   assert actual_status_code == int(status_code)

@Then ("User sends DELETE request")
  def step_impl(context):
    url = "/api/users/2"
    headers = {'accept': “application/json”}
    response = requests.request("DELETE", url, headers=headers, verify=False)
    
    actual_status_code = response.status_code
    assert actual_status_code == int(status_code)
    
    cnxn = pyodbc.connect("DSN=REQRES")
    cursor = cnxn.cursor()
    cursor.tables()
    rows = cursor.fetchall()
    print("No user found")
