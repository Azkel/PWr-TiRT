import dpkt


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
