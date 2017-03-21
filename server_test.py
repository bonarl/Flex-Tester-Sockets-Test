# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:51:14 2017

@author: bonar
"""

import socket
from port_finder import listSerialPorts
from Expander import EXPANDER
import serial
import time
import datetime                                     
import flex_tools
from flex_tools import *

                                      

#Flex-Tape network
#all pins on all boards are named according to the network they belong to

com_ports = listSerialPorts().reverse()

flex_tape = FLEX_TAPE(network, board_names)

# create a socket object, this allows multiple computers to be used for board reading
#using parse_net function of flex_tape. Specify which board is connected to other
#pi in net_parse function
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)      
host = socket.gethostname()                           
port = 5000                          
serversocket.bind((host, port))                                  
serversocket.listen(5)   

print('waiting for connection')
clientsocket,addr = serversocket.accept()      
print("Got a connection from %s" % str(addr))
flex_tape.net_parse('P1', 'P2', com_ports, baudrate, clientsocket, 'P6')
net = flex_tape.net()

serversocket.close()

