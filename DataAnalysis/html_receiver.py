import socket
import errno
from socket import error as SocketError
import analysis_sender
import time

def listen():
    tcp_ip = '127.0.0.1'
    tcp_port = 5006
    buffer_size = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((tcp_ip, tcp_port))
    s.listen(1)
    conn, addr = s.accept()
    while 1:
        try:
            data = conn.recv(buffer_size)
            if not data:
                break
            # images_analyzer.analyze(data)
            # css_class_analyzer.analyze(data)
            # tags_analyzer.analyze(data)
            # links_analyzer.analyze(data)
            time.sleep(0.3)
            analysis_sender.images(data)
            analysis_sender.css_classes(data)
            analysis_sender.tags(data)
            analysis_sender.links(data)
            # conn.send("+")  # echo
        except SocketError as e:
             if e.errno != errno.ECONNRESET:
                raise  # Not error we are looking for
        pass  # Handle error here.