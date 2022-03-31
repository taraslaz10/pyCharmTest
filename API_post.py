import requests

response = requests.post('https://pythonexamples.org/',
            data = {'key1':'value1', 'key2':'value2'})
print(response.headers)