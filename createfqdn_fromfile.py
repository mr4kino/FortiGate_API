#!/usr/bin/env python
import requests
import json


url = 'https://10.0.a.b/'
name = 'admin'
password = 'admin'


client = requests.session() 

requests.packages.urllib3.disable_warnings()

api_cmdb = 'api/v2/cmdb/'
api_monitor = 'api/v2/monitor/'

List_FQDN = open("/home/user/Documents/fqdn_extracted.log", "r")



try:
	login = client.post(url + '/logincheck', data="username=" + name + "&secretkey=" + password, verify = False)
except requests.exceptions.ConnectionError:
	requests.status_code = "Connection refused"

ini = client.cookies['ccsrftoken']
csrftoken = ini[1:-1]
client.headers.update({"X-CSRFTOKEN": csrftoken})

address = []
for fqdn in List_FQDN:
	a = fqdn.strip('\n')
	fqdn_json = {"name":"Test_FQDN_%s" % a, "type":"fqdn", "fqdn":"%s" % a} 
	print fqdn_json
	address.append(fqdn_json)

for i in address:
	print i
	ae = client.post(url + api_cmdb + 'firewall/address/', verify = False, params = {'vdom': 'root'}, json={'json': i})

List_FQDN.close()
client_logout = client.post(url + '/logout', verify = False)
client.close()




