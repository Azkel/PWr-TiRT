import dpkt


def filter_frames(data):
    filtered_data = []
    for frame in data:
        eth = dpkt.ethernet.Ethernet(frame)
        if dpkt.ethernet.ETH_TYPE_IP == eth.type:
            filtered_data.append(eth.data)
    return filtered_data
