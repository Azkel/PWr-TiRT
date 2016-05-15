import dpkt
import socket
import pickle

def listen():
    tcp_ip = '127.0.0.1'
    tcp_port = 5006
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
    values = filter_frames(stream_list)
    print len(values)
    print 'Tyle zostalo'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port+1))
    for element in values:
        s.send(element)
        print 'dupa'
        echo = s.recv(buffer_size)
    s.close()


def filter_frames(data):
    filtered_data = []
    for frame in data:
        eth = dpkt.ethernet.Ethernet(frame)
        if dpkt.ethernet.ETH_TYPE_IP == eth.type:
            filtered_data.append(frame)
    return filtered_data

while 1:
    listen()
