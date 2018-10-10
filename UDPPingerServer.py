# UDPPingerServer.py
# We will need the following module to generate randomized lost packets

import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12005))

while True:        
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)   
    message = message.upper()
     
    if rand < 4:
        continue

    serverSocket.sendto(message, address)
