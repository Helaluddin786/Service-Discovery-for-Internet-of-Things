#!/usr/bin/env python
import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

__author__ = ''

client = None


def usage():  # pragma: no cover
    print "Command:\tcoapclient.py -o -p [-P]"
    print "Options:"
    print "\t-o, --operation=\tGET|PUT|POST|DELETE|DISCOVER|OBSERVE"
    print "\t-p, --path=\t\t\tPath of the request"
    print "\t-P, --payload=\t\tPayload of the request"
    print "\t-f, --payload-file=\t\tFile with payload of the request"


def client_callback(response):
    print "Callback"


def client_callback_observe(response):  # pragma: no cover
    global client
    print "Callback_observe"
    check = True
    while check:
        chosen = raw_input("Stop observing? [y/N]: ")
        if chosen != "" and not (chosen == "n" or chosen == "N" or chosen == "y" or chosen == "Y"):
            print "Unrecognized choose."
            continue
        elif chosen == "y" or chosen == "Y":
            while True:
                rst = raw_input("Send RST message? [Y/n]: ")
                if rst != "" and not (rst == "n" or rst == "N" or rst == "y" or rst == "Y"):
                    print "Unrecognized choose."
                    continue
                elif rst == "" or rst == "y" or rst == "Y":
                    client.cancel_observing(response, True)
                else:
                    client.cancel_observing(response, False)
                check = False
                break
        else:
            break


def main():  # pragma: no cover
    global client
    op = None
    path = None
    payload = None
    pathArray =  ["aaaa::212:7404:4:404"
	]
	
    
    
    total = 0;
    count = 0;
    file = open('services.txt','w')
    for i in range(1):
	path = "coap://["+pathArray[0]+"]:5683/"
	host, port, path = parse_uri(path)
    	try:
        	tmp = socket.gethostbyname(host)
        	host = tmp
    	except socket.gaierror:
        	pass
    	client = HelperClient(server=(host, port))
	start = time.time()
	print(count)   

	response = client.discover()
        

	dtime = time.time()-start
	file.write(str(dtime)+'\n')
	total = total + dtime
	count = count+1
	time.sleep(0.6)
        print (response.pretty_print())
    avgTime = total/100
    file.write('services = '+str(response))
    print('AVG='+str(response))
    file.close()
    client.stop()
   


if __name__ == '__main__':  # pragma: no cover
    main()
