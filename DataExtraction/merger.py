import dpkt
import socket
import pickle

def compare_by_sequence(a, b):
    return int(a.seq - b.seq)


def ip_address(bytes):
    return ".".join([str(ord(b)) for b in bytes])


def tcp_streams(datagrams):
    streams = {}
    for d in datagrams:
        if d.p != dpkt.ip.IP_PROTO_TCP:
            continue
        tcp = d.data
        k = (ip_address(d.src), tcp.sport, ip_address(d.dst), tcp.dport)
        if k in streams:
            streams[k].append(tcp)
        else:
            streams[k] = [tcp]

    for s in streams:
        try:
            streams[s].sort(compare_by_sequence)
            d = []
            for p in streams[s]:
                try:
                    d.append(p.data)
                except AttributeError, e:
                    pass
            streams[s] = "".join(d)
        except TypeError, e:
            print "Packet:", type(e), str(e)

    return streams


def listen():
    tcp_ip = '127.0.0.1'
    tcp_port = 5008
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
        stream_list.append(dpkt.ethernet.Ethernet(data).data)
        conn.send("+")  # echo
    values = tcp_streams(stream_list)
    print len(values)
    print 'Tyle zostalo'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port+1))
    for element in values:
        s.send(pickle.dumps(element))
        print 'dupa'
        echo = s.recv(buffer_size)
    s.close()

while 1:
    listen()
