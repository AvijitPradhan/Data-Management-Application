@apispec

Feature: This feature is for creating a new User by POST and verify using GET.
  
  Scenario Outline: Create using POST/api/users and verify the same using GET/api/users/id
    Given User has all the prerequisites for POST and GET requests
    When User sends POST requests
    Then User should be created
    Then User sends GET request
    Then User details should be displayed
    Then User sends DELETE request
    And User details should be deleted.
   
