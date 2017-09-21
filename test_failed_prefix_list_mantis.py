#!/usr/bin/env python
import requests
import json

url = 'https://10.0.2.45/'
name = 'yazrak'
password = 'password'

client = requests.session() 

api_cmdb = 'api/v2/cmdb/'
api_monitor = 'api/v2/monitor/'


prefixlists = [
            {"name":"default_only","rule":[{"prefix":"0.0.0.0 0.0.0.0"}]},
            {"name":"dwre_sf_block6","rule":[{"prefix":"10.254.165.0 255.255.255.0","ge":25, "le":28}]},
            {"name":"dwre_sf_block6443","rule":[{"prefix":"10.254.167.0 255.255.255.0","ge":25, "le":28}]}
          ]
prefixlists1 = [{"name":"Test_mantis","rule":[{"prefix":"10.254.169.0 255.255.255.0","ge":25, "le":28}]}]

data1 = prefixlists[1]
data2 = prefixlists1[0]
login = client.post(url + '/logincheck', data="username=" + name + "&secretkey=" + password, verify = False)
ini = client.cookies['ccsrftoken']
csrftoken = ini[1:-1]
client.headers.update({"X-CSRFTOKEN": csrftoken})
#ae = client.put(url + api_cmdb + 'router/prefix-list/dwre_sf_block6/', verify = False, params = {'vdom': 'root'}, json={'json': data1)
ae = client.post(url + api_cmdb + 'router/prefix-list/', verify = False, params = {'vdom': 'root'}, json={'json': data2})
ad = client.post(url + '/logout', verify = False)
client.close()
