#!/usr/bin/env python
import requests
import json


url = 'https://10.0.2.45/'
name = 'yazrak'
password = 'pecpedal'

client = requests.session() 

api_cmdb = 'api/v2/cmdb/'
api_monitor = 'api/v2/monitor/'

login = client.post(url + '/logincheck', data="username=" + name + "&secretkey=" + password, verify = False)
ini = client.cookies['ccsrftoken']
csrftoken = ini[1:-1]
client.headers.update({"X-CSRFTOKEN": csrftoken})

address = []
for x in range (0,20):
	for y in range (1,10):
		ip = {"name":"Test_RestAPI_Python_%d_%d" % (x,y),"subnet":"185.54.%d.%d 255.255.255.255" % (x,y),"type":"ipmask"} 
		address.append(ip)

for i in address:
	print i
	ae = client.post(url + api_cmdb + 'firewall/address/', verify = False, params = {'vdom': 'root'}, json={'json': i})

client.close()

