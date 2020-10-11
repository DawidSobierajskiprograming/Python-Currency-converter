import json
import requests

url = 'https://api.exchangeratesapi.io/latest'

isitup = requests.get(url)
print (isitup.status_code)