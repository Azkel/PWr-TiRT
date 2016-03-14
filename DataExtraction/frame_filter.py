import dpkt


def filter_frames(data):
    filtered_data = []
    for frame in data:
        eth = dpkt.ethernet.Ethernet(frame)
        if eth.type == dpkt.ethernet.ETH_TYPE_IP or eth.type == dpkt.ethernet.ETH_TYPE_IP6:
            filtered_data.append(frame)
    return filtered_data
