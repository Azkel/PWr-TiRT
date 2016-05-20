import html_receiver
import images_server
import css_class_server
import tags_server
import links_server

def start_html_receiver():
    while 1:
        html_receiver.listen()

def start_images_server():
    while 1:
        images_server.listen()

def start_css_class_server():
    while 1:
        css_class_server.listen()

def start_tags_server():
    while 1:
        tags_server.listen()

def start_links_server():
    while 1:
        links_server.listen()
