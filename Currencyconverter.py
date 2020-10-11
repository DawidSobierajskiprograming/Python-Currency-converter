import json
import requests
import urllib.parse

url = 'https://api.exchangeratesapi.io/latest'

json_data = requests.get(url).json()

print("For 1 " + json_data['base'] + " You can have")
print()
print( str(json_data['rates']['PLN']) + " Polish Zloty")

