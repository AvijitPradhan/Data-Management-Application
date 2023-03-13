from behave import *
from selenium.webdriver.common.keys import keys

@given("User is able to navigate to https://reqres.in/")
 def step_impl(context):
    driver.get('https://reqres.in/')
    
@when ("User taps on any request on homepage")
 def step_impl(context):
    driver.click('button')
   
@then("Then User see different request types and endpoints")
 pass
.
.
@then("Then User can see a Button to navigate to Support Page")
 def step_impl(context):
  select = select(driver.find_element(byname,'supportpage')
                  
@then("User can see 'One Time' and 'Monthly' payment  option in Support page")
  def step_impl(context):
   select = select.select_by_index(index)
 
@And("user see the Upgrade button options")
    def step_impl(context):
     element = driver.find_element(By.name, "source")
