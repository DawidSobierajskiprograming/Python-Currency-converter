import json
import requests
import urllib.parse
import datetime
from datetime import datetime

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
    date_with_time = datetime.strptime(request_date, '%d/%m/%Y')
    date_only_date = date_with_time.date()
    url = url_base.format(date_only_date)
    Json_date = requests.get(url).json()
    dateurl = requests.get(url)
    
    print ("With Euro as the Base. The rates on " + request_date + " are:")
    print ("---------------------------------------------------------")
    print()

    for each in Json_date['rates']:
        print(each + ": " + str(Json_date['rates'][each]))

def convert():
    request_start_currency = input("What currency are you converting from? ")
    request_ammount = input("How much " + request_start_currency + " are you looking to convert? ")
    request_end_currency = input ("What is the currecny you want the value for? ")

    formatted_url = url_base.format('latest?')
    url = formatted_url + urllib.parse.urlencode({"base": request_start_currency})
    Json_Rates = requests.get(url).json()

    end_currecny_value = Json_Rates.get(request_end_currency)
    if end_currecny_value != None:
        total_value = end_currecny_value * request_ammount
        print ("If you have " + request_ammount + " " + request_start_currency + " Then you will have " + total_value + " " + request_end_currency)
    else:
        print ("Sorry we don't have infomration on this currency")


print (" Welcome to Currency info ")
print ("--------------------------")

while True:
    usr_question = input ("What currency questions do you have? ")

    if usr_question == "rates" or usr_question == "Rates":
        rates_with_base()
    
    elif usr_question == "date":
        rates_at_date()
    
    elif usr_question == "convert":
        convert()
    
    elif usr_question == "q" or usr_question == "quit":
        break
