import json
import requests

key = 'b145d818a00b68effae484424ff20590'
apihome = 'http://data.fixer.io/api/'

headers = {'Content-Type':'application/json',
            'Authorization': 'Bearer {0}'.format(key)}

def getlatest():

    api_url = '{0}latest'.format(apihome)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))

    else: return None

latestval = getlatest()

if latestval is not None:
    print("Here are all the latest values for the currencies ")
    for k, v in latestval['latest'].items():
        print('{0}:{1}'.format(k,v))

else:
    print("[!] Request Failed")