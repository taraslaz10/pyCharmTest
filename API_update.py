import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.put("https://reqres.in/api/register", data = payload)
print(response)
print(response.json())