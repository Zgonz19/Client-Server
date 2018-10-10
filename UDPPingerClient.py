#Gonzalo Zepeda    Socket Programming Assignment 2: UDP
#UDPPingerClient.py
import time
from socket import *

pings = 1

#Send 10 Pings to the UDP server
while pings < 11:

    #New UDP socket created
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #timeout value set to 1 second
    clientSocket.settimeout(1)

    #message sent to server
    message = 'ping successful'

    addr = ("127.0.0.1", 12005)

    #Start a timer and send ping to the corresponding address
    start = time.time()
    clientSocket.sendto(message, addr)

    #If data is received back from server, print 
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print 'Ping:',pings, '       Server Response:',data, '        RTT:',elapsed



    #If data is not received back from server
    except timeout:
        print 'REQUEST TIMED OUT'

    pings = pings + 1
