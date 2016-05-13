import socket
import errno
from socket import error as SocketError
import images_analyzer
import css_class_analyzer
import tags_analyzer
import links_analyzer
# import analysis_sender

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
            images_analyzer.analyze(data)
            css_class_analyzer.analyze(data)
            tags_analyzer.analyze(data)
            links_analyzer.analyze(data)
            # analysis_sender.images(data)
            # conn.send("+")  # echo
        except SocketError as e:
             if e.errno != errno.ECONNRESET:
                raise  # Not error we are looking for
        pass  # Handle error here.