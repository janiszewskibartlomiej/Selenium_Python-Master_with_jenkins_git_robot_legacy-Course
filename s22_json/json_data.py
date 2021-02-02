import requests
import json
# import jsonpath

api_url = "https://reqres.in/api/users?page=2"

# Make a request
response1 = requests.get(api_url)
print(response1.text)

# Validate Status code
assert response1.status_code == 200

# Parse response into JSON format
json_response = json.loads(response1.text)

print(json_response)
print(json_response["data"][0]["email"])
# Apply JSON Path
# x = jsonpath.jsonpath(json_response, 'total')
# print(x[0])
# y = jsonpath.jsonpath(json_response, 'data[2].last_name')
# print(y[0])

for val in json_response['data']:
    print(val['first_name'])