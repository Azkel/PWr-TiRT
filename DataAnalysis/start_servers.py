import html_receiver
# import images_server

def start_html_receiver():
    while 1:
        html_receiver.listen()

def start_images_server():
    while 1:
        images_server.listen()