import requests

i =requests.get('https://www.facebook.com/')
print(i)
response = requests.get('https://api.github.com')
print(response)
