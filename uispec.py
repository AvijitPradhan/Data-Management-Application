from behave import *
from selenium.webdriver.common.keys import keys

@given("User is able to navigate to https://reqres.in/")
 def step_impl(context):
    driver.get('https://reqres.in/')
    
 pass
