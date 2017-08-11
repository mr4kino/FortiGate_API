#!/usr/bin/env python
import requests, json, sys

# here we get the authentication token and we store this cookie in a cookies.txt file

url = 'http://10.0.2.45/'
name = 'admin'
password = 'abcdefg'

#all cookies received will be stored in the session object
client = requests.session() 

print 'client headers initially: ', client.headers, '\n \n'
print 'client cookies initially: ', client.cookies, '\n \n'

#First connection used for authentication.
login = client.post(url + '/logincheck', data="username=" + name + "&secretkey=" + password, verify = False)

#csrftoken to be inserted in the headers for next put,post,delete requests. This will be stored in csrftoken variable. 
#On the FGT it is named ccsrftoken (double c)
#csrftoken = client.cookies['ccsrftoken']
print 'client cookies after login: ', client.cookies, '\n \n'
print 'csrftoken value extracted from the cookie: ', client.cookies['ccsrftoken'], '\n \n'

#for initial debugging: we print the values that has been stored for the crsftoken value.
#print csrftoken
#print client.cookies

#for debugging, we print the headers variable value
#print headers
#print '\n \n \n'

client.headers.update({"X-CSRFTOKEN": client.cookies['ccsrftoken']})
print client.headers


get_cmdb = client.get(url + 'api/v2/cmdb/firewall/address?vdom=root', verify = False)

#This will print out the values that we got from the Firwall. In this case the address entries in the root vdom
print get_cmdb.text

print '\n'

#we try to post, ie create, a firewall address
addresstest = {'name':"address13", 'type': "ipmask", 'subnet': "1.1.1.0 255.255.255.0"}
api_cmdb = 'api/v2/cmdb/'
c = client.post(url + api_cmdb + 'firewall/address?vdom=root', verify = False)
print '\n'
#print c.text


client.close()
#print b