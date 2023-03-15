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
    context.element = driver.find_element_by_id("users")
    context.element.click()
   
@then("User see different request types and endpoints")
 def step_impl(context):
    context.element = driver.find_element_by_id("users", "users-single", "users-single-not-found","unknown", "unknown-single","unknown-single-not-found", "post","put","patch", "delete")
    context.element.click()
    
@then("user can see Sample request and response details for different request types")
 def step_impl(context):
  m = driver.find_element_by_xpath("//span[@class='url']")
#verify if element present
  b = m.is_displayed()
   if b:
    print("Element with span class available")
   else:
    print("Element with span class not available")
   context.response = driver.find_element_by_xpath(//*[@class='response-code'])
   print(context.response)
  
  context.responsedata = driver.find_element_by_xpath(//*[contains(@data-key,'output-response')
   print(context.responsedata)                                                       
                                                   
@then("User can see a Button to navigate to Support Page")
 def step_impl(context):
   context.element = driver.find_element_by_id("support-heading")                                                    
    print(context.element())
                                                          
@then("user see One Time payment option in Support page")
  def step_impl(context):
   context.button =driver.find_element_by_xpath("//input[@id='supportOneTime']")
   context.element.click()
                                                          
@then("user see Monthly payment option in Support page")
  def step_impl(context):
   context.button =driver.find_element_by_xpath("//input[@id='supportRecurring']")
                                                          
@and("user sees the Upgrade button options after support page")
   def step_impl(context):
    context.element = driver.find_element_by_id("trigger-pro")                                                    
    context.element.click()                                                      
                                                          
                                                          
                                                          
