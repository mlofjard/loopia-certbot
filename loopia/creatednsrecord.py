#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
  
import sys  
import ssl
import xmlrpc.client

def main():  
    global_username = sys.argv[3]
    global_password = sys.argv[4]
    global_domain_server_url = 'https://api.loopia.se/RPCSERV'   
  
    domain = 'lofjard.se'
    sub_domain = sys.argv[5]
  
    zone_recone = { 'type': 'TXT',
                    'ttl': 300,
                    'priority': 0,
                    'rdata': sys.argv[1],
                    'record_id': 0
                  }

    zone_rectwo = { 'type': 'TXT',
                    'ttl': 300,
                    'priority': 0,
                    'rdata': sys.argv[2],
                    'record_id': 0
                  }

    context = ssl.create_default_context()
    client = xmlrpc.client.ServerProxy(global_domain_server_url, encoding = 'utf-8', context = context, verbose = True)
  
    response = client.addZoneRecord(global_username, global_password, domain, sub_domain, zone_recone)   
    print ('Zone record added: %s\n' % response)  
    response = client.addZoneRecord(global_username, global_password, domain, sub_domain, zone_rectwo)
    print ("Zone record added: %s\n" % response)

if __name__ == '__main__':  
    main() 
