#!/usr/bin/env python

import socket


def listen():
    tcp_ip = '127.0.0.1'
    tcp_port = 5005
    buffer_size = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((tcp_ip, tcp_port))
    s.listen(1)
    stream_list = []
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(buffer_size)
        if not data:
            break
        stream_list.append(data)
        conn.send("+")  # echo
    conn.close()
    return stream_list
