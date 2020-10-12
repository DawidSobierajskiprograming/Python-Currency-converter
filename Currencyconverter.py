import json
import requests
import urllib.parse
import datetime
from datetime import *

url_base = 'https://api.exchangeratesapi.io/{}'

def rates_with_base():
    
    base = input("What base currency would you like to use? ")
    formatted_url = url_base.format('latest?')
    url = formatted_url + urllib.parse.urlencode({"base": base})
    Json_Rates = requests.get(url).json()

    print ("With " + base + " as the base todays rates are")
    print ("----------------------------------------------")
    print ()
    
    for each in Json_Rates['rates']:
        print (each + ": " + str(Json_Rates['rates'][each]))

def rates_at_date():

    request_date = input("What Date would like to have information on? ")
    date_formatted = datetime.strptime(request_date, '%d/%m/%Y')
    print (date_formatted)

print (" Welcome to Currency info ")
print ("--------------------------")

while True:
    usr_question = input ("What currency questions do you have? ")

    if usr_question == "rates" or usr_question == "Rates":
        rates_with_base()
    
    elif usr_question == "date":
        rates_at_date()
    
    elif usr_question == "q" or usr_question == "quit":
        break
