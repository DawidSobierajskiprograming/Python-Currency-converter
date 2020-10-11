import json
import requests

url = 'https://api.exchangeratesapi.io/latest?base=GBP'

isitup = requests.get(url)
jresponse = isitup.json()
print(jresponse)