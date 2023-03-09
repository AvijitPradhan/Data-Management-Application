@uispec

Feature: Navigate to 'https://reqres.in/' with all request types and endpoints
  
  Scenario Outline: User should navigate to 'https://reqres.in/' and can click on request types and endpoints.
    Given User is able to navigate to https://reqres.in/
    When User taps on any request on homepage
    Then User see different request types and endpoints
    .
    .
    Then user see payment options
    And user see the Upgrade button options
 


