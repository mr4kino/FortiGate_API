#!/usr/bin/env python
import requests, json, sys

# here we get the authentication token and we store this cookie in a cookies.txt file

url = 'http://10.0.2.45/'
name = 'admin'
password = 'abcdefg'

#all cookies received will be stored in the session object
client = requests.session() 


#First connection used for authentication.
login = client.post(url + '/logincheck', data="username=" + name + "&secretkey=" + password, verify = False)

#csrftoken to be inserted in the headers for next put,post,delete requests. This will be stored in csrftoken variable. 
#On the FGT it is named ccsrftoken (double c)
ini = client.cookies['ccsrftoken']
csrftoken = ini[1:-1] # this is to remove the double quote

client.headers.update({"X-CSRFTOKEN": csrftoken})


get_cmdb = client.get(url + 'api/v2/cmdb/firewall/address?vdom=root', verify = False)

#This will print out the values that we got from the Firwall. In this case the address entries in the root vdom
print get_cmdb.text

print '\n'


client.close()

