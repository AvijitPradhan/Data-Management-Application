@uispec

Feature: Navigate to 'https://reqres.in/' with all request types and endpoints
  
  Scenario Outline: User should navigate to 'https://reqres.in/' and can click on request types and endpoints.
    Given User is able to navigate to https://reqres.in/
    When User taps on any request on homepage
    Then User see different request types and endpoints
    .
    .
    Then User can see a Button to navigate to Support Page
    Then user see payment options
    Then User can see 'One Time' and 'Monthly' payment  option in Support page
    And user see the Upgrade button options
 


