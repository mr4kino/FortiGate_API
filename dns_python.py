#!/usr/bin/env python

from __future__ import print_function
import dns.resolver


#File containing the FQDNs
List_FQDN = open("/home/user/Documents/fqdn_extracted.log", "r")

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

for fqdn in List_FQDN:
	a = fqdn.strip('\n')
	print (a)

	try:
		answers = dns.resolver.query(a, 'A')
		for rdata in answers:
			print(rdata)
	except (dns.resolver.NXDOMAIN):
		print("Couldn't find any records (NXDOMAIN)") 
	except (dns.resolver.NoAnswer):
		print("Couldn't find any records (NoAnswer)")
	except (dns.resolver.NoNameservers):
		print(": All nameservers failed to answer the query" + a + "IN A: Server 8.8.8.8 UDP port 53 answered REFUSED")
	print("\n\n")
	
List_FQDN.close()
