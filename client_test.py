# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:53:42 2017

@author: bonar
"""

import socket
import time
import flex_tools
from flex_tools import *
import json
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 5000
s.connect((host, port)) 

#open serial with board

while True:
    
    own_net = net[board.decode('utf-8')]

    
    for i in range(40):
        msg = s.recv(1024)
        if msg == go:
            print('reading board')
            result = check_real(brd)
            b = json.dumps(result).encode('utf-8')
            s.sendall(b)      
            #server marks checked, stores results in server dictionary
        
        
    break
                        
s.close()

