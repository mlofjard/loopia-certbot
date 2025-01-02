#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
  
import sys  
import ssl
import xmlrpc.client

def main():  
    global_username = sys.argv[1]
    global_password = sys.argv[2]
    global_domain_server_url = 'https://api.loopia.se/RPCSERV'   
  
    domain = 'lofjard.se'
    sub_domain = '_acme-challenge.int'
  
    context = ssl.create_default_context()
    client = xmlrpc.client.ServerProxy(global_domain_server_url, encoding = 'utf-8', context = context)
  
    allRecords = client.getZoneRecords(global_username, global_password, domain, sub_domain)  
    for record in allRecords:
        response = client.removeZoneRecord(global_username, global_password, domain, sub_domain, record['record_id'])  
        print ('Zone record removed: %s\n' % response)  
  
if __name__ == '__main__':  
    main()  
