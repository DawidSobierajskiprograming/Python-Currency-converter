# Python-Currency-converter

This is a short program that can return you the values of currencies today, the value of a certain currency on a specified date, and it will let you convert a certain amount of a specified currency to the amount it is worth in a different currency.
examples:
- All values today
- GBP value on 08/03/2010
- how much JPY can i get for 400 GBP

The first function works by simply requesting all the rates for today from the api and then going through each one and printing both the key which is the currency and the value of the currency today.
The second function works by requesting the base currency, and the date that the user asks for and then it converts the given date to a functional date that can then be added to the end of the url and then it requests the rates from the api and does the same thing that the first function does.
The third function takes a given base currency, the amount of the base currency and the currecny they want the value in then it adds the base currecny to the url so that the rates returned by api are based on the base currency, then the base currency value is multiplied by the value that is given in the base currency and the output of those two is put in the final return.