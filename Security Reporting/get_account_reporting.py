#get_account_reporting.py

import http.client
import socket
import requests
import json
import http.client

#Add Auth Token Here:
api_token = 'jwtAuthToken=<<Add Token Here>>'


api_url_base = 'https://prepareyourmeal-dev-api.prepareyourmeal.rasodu.com/admin/loginhistory?'
headers = {'jwtAuthToken': api_token}

store_list = []

response = requests.get(api_url_base + api_token)

#print(response.json())

#print('\n\n')

#print('JSON:' + json.dumps(response.json()))

json_array = json.dumps(response.json())
json_array2 = response.json()

users = []
logintime = []
realtime = []

for user in json_array2:
    #print(user['username'])

    try:
        #print(user['latestLogedInDate'])

        logintime.append(user['username'] + ' \t| ' + (user['latestLogedInDate']) + '\t|')

    except:
        #print('null')
        logintime.append(user['username'] + ' \t| ' +'null' + '\t|')


print('\n//------------------------------------------------')
print('| User Name \t| Last Logged In \t')
print('//------------------------------------------------')

for login in logintime:
    print(login)
