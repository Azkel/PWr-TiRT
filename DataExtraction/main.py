#!/usr/bin/python

import receiver
import html_extractor
import merger
import socket
import dpkt


def filter_frames(data):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5006
    BUFFER_SIZE = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    for element in data:
        s.send(element)
        echo = s.recv(BUFFER_SIZE)
    s.close()
    new_data = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT+1))
    s.listen(1)
    conn, addr = s.accept()
    while 1:
        received_data = conn.recv(BUFFER_SIZE)
        if not received_data:
            break
        new_data.append(received_data)
        conn.send("+")  # echo
    conn.close()
    return new_data


def extract_ethernet(packets):
    extracted_data = []
    for frame in packets:
        eth = dpkt.ethernet.Ethernet(frame)
        extracted_data.append(eth.data)
    return extracted_data

while 1:
    data = receiver.listen()
    print 'Received frames:', len(data)
    print 'Filtering TCP/IP frames...'
    data = filter_frames(data)
    print 'After filtering there are ', len(data), ' left.'
    data = extract_ethernet(data)
    data = merger.tcp_streams(data)
    html_extractor.forward_html(data)
