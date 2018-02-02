#!/usr/bin/env python
import requests


url = 'https://10.0.a.b/'
name = 'admin'
password = 'password'

client = requests.session() 



login = client.post(url + '/logincheck', data="username=" + name + "&secretkey=" + password, verify = False)

ini = client.cookies['ccsrftoken']
csrftoken = ini[1:-1]

client.headers.update({"X-CSRFTOKEN": csrftoken})



api_cmdb = 'api/v2/cmdb/'
api_monitor = 'api/v2/monitor/'


i = 0
while i < 100:
	ab = client.get(url + api_cmdb + 'vpn.ipsec/phase1-interface/ZG-FIB-VDSL', verify = False, params = {'vdom': 'root'})
	ac = client.get(url + api_monitor + 'vpn/ipsec/select?tunnel=ZG-FIB-VDSL', verify = False, params = {'vdom': 'root'})
	i += 1

client.close()