import dpkt
import StringIO
import gzip
import socket
import string
import random
from StringIO import StringIO

def forward_html(data):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5006
    BUFFER_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    for key, value in    data.iteritems():
        HTTP_PORT = 80
        is_HTTP = (key[1] == HTTP_PORT or key[3] == HTTP_PORT)
        if is_HTTP:
            is_response = value.startswith("HTTP")
            if is_response:
                try:
                    http = dpkt.http.Response(value)
                    if 'content-encoding' in http.headers and http.headers.pop('content-encoding') == 'gzip':
                        buf = StringIO(http.body)
                        f = gzip.GzipFile(fileobj=buf)
                        http_decoded = f.read()
                    else:
                        http_decoded = http.body
                    if http is not None and http.body is not None:
                        s.send(http_decoded)
                    if 'content-type' in http.headers and http.headers.pop('content-type') == 'image/png':
                        fh =open("extractedImages/"+  randomword(10) + ".png","wb")
                        fh.write(http_decoded)
                        fh.close()

                except dpkt.NeedData:
                    print "Parsing error encountered"

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))