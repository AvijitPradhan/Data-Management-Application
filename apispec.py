
import requests

@given("User has all the prerequisites for POST and GET requests")

*** Environment files should be initialized ***

@When ("User sends POST requests")

import requests
url = "/api/users/"
payload =
"{\"user\":{\"email\":\"admin@xyz.com\",\"password\":\"admin123 4\"}}"
headers = {
'accept': “application/json”,
...}
response = requests.request("POST", url, data=payload, headers=headers, verify=False)
print(response.text)

 @then ("User should be created")
 
import odbc

@Then ("User sends GET request")

response = requests.request("GET", url,params=querystring, headers=headers, verify=False)

@Then ("User sends DELETE request")

response = requests.request("DELETE", url, headers=headers, verify=False)
