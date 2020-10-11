import json
import requests
import urllib.parse

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

print (" Welcome to Currency info ")
print ("--------------------------")

usr_question = input ("What currency questions do you have? ")

if usr_question == "rates" or usr_question == "Rates":
    rates_with_base()