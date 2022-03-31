import requests

resp = requests.get('https://reqres.in/api/users?page/2')

code = resp.json()

print(code['total'])