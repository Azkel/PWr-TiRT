#!/usr/bin/env python

import socket
import sys
import pcap
import pickle

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

p = pcap.pcap('testn.pcap')
for ts, pkt in p:
    s.send(pkt)
    data = s.recv(BUFFER_SIZE)
    print data
s.close()
