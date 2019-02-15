############################################################################
#                                                                          #
# Copyright (c)2009, Digi International (Digi). All Rights Reserved.       #
#                                                                          #
# Permission to use, copy, modify, and distribute this software and its    #
# documentation, without fee and without a signed licensing agreement, is  #
# hereby granted, provided that the software is used on Digi products only #
# and that the software contain this copyright notice,  and the following  #
# two paragraphs appear in all copies, modifications, and distributions as #
# well. Contact Product Management, Digi International, Inc., 11001 Bren   #
# Road East, Minnetonka, MN, +1 952-912-3444, for commercial licensing     #
# opportunities for non-Digi products.                                     #
#                                                                          #
# DIGI SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED   #
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A          #
# PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, #
# PROVIDED HEREUNDER IS PROVIDED "AS IS" AND WITHOUT WARRANTY OF ANY KIND. #
# DIGI HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,         #
# ENHANCEMENTS, OR MODIFICATIONS.                                          #
#                                                                          #
# IN NO EVENT SHALL DIGI BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,      #
# SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS,   #
# ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF   #
# DIGI HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.                #
#                                                                          #
############################################################################

"""\
    
    XBee server for sending sensor data when requested
    
"""

import sys, os 
import time
from socket import *

import xbeelib.xbeelt

# Create sensor objects
sensor_addresses = ["[00:13:a2:00:41:63:87:88]!",
                    "[00:13:a2:00:41:4f:ad:92]!",
                    "[00:13:a2:00:41:4f:ad:97]!"]
sensors = [xbeelib.xbeelt.XBeeLTN(addr) for addr in sensor_addresses]

# Setup socket
recvSize = 1024
addr = ("", 13000)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

while True:

    # wait for someone to request data
    #print("waiting for transmission...")
    (data, addr) = UDPSock.recvfrom(recvSize)
    data = data.decode('utf-8')
    #print("TRANSMISSION: " + data)

    # (do something with request) #

    # Retrieve data from sensors
    sendBuf = ""
    samples = [sensor.sample() for sensor in sensors]
    for i in range(len(samples)):
    	# add 1 to index for human readability
        sendBuf += "L" + str(i+1) + "=" + str(samples[i]['light']) + "\n"
        sendBuf += "T" + str(i+1) + "=" + str(samples[i]['temperature']) + "\n"
        sendBuf += "H" + str(i+1) + "=" + str(samples[i]['humidity']) + "\n"

    # send data
    #print("sending transmission...")
    targetAddr = (addr[0], 13000)
    UDPSock.sendto(sendBuf, targetAddr)
    
    #time.sleep(3)
