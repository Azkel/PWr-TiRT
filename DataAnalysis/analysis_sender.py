import socket


def images(data):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5007
    BUFFER_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(data)
    s.close()

def css_classes(data):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5008
    BUFFER_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(data)
    s.close()

def tags(data):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5009
    BUFFER_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(data)
    s.close()

def links(data):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5010
    BUFFER_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(data)
    s.close()
