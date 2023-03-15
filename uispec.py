from behave import *
from selenium.webdriver.common.keys import keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

@given("User is able to navigate to https://reqres.in/")
 def step_impl(context):
    service = Service(executable_path="/usr/local/bin/chromedriver")
    with webdriver.Chrome(service=service) as driver:
    driver.get('https://reqres.in/')
    
@when ("User taps on any request on homepage")
 def step_impl(context):
    element = driver.find_element_by_id("users")
    element.click()
   
@then("Then User see different request types and endpoints")
 def step_impl(context):
    element = driver.find_element_by_id("users", "users-single", "users-single-not-found","unknown", "unknown-single","unknown-single-not-found", "post","put","patch", "delete")
    element.click()
    
@then("Then User can see a Button to navigate to Support Page")
 def step_impl(context):
  select = select(driver.find_element(byname,'supportpage')
                  
@then("User can see 'One Time' and 'Monthly' payment  option in Support page")
  def step_impl(context):
   select = select.select_by_index(index)
 
@And("user see the Upgrade button options")
    def step_impl(context):
     element = driver.find_element(By.name, "source")
