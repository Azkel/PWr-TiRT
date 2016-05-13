#from html.parser import HTMLParser
from HTMLParser import HTMLParser
import os.path
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime


class LinksParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list = dict()
        self.list['external link'] = 0
        self.list['internal link'] = 0
        self.list['external js'] = 0
        self.list['internal js'] = 0
        self.list['inline js'] = 0
        self.list['external css'] = 0
        self.list['internal css'] = 0
        self.list['inline css'] = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            link = dict(attrs)["href"]
            if link.startswith(('http', 'ftp', 'www')):
                self.list['external link'] += 1
            else:
                self.list['internal link'] += 1
        elif tag == 'script':
            if 'src' in dict(attrs):
                link = dict(attrs)["src"]
                if link.startswith(('http', 'ftp', 'www', '//')):
                    self.list['external js'] += 1
                else:
                    self.list['internal js'] += 1
            else:
                self.list['inline js'] += 1
        elif tag == 'link':
            if dict(attrs)['rel'] == 'stylesheet':
                if 'href' in dict(attrs):
                    link = dict(attrs)["href"]
                    if link.startswith(('http', 'ftp', 'www', '//')):
                        self.list['external css'] += 1
                    else:
                        self.list['internal css'] += 1
                else:
                    self.list['inline css'] += 1



def analyze(data):
    h=LinksParser()
    # page='<!DOCTYPE html><html><body><h2>Spectacular Mountain</h2><img src="pic_mountain.jpg" alt="Mountain View" style="width:304px;height:228px;"><img src="pic_mountain.jpg" alt="Mountain View" style="width:304px;height:228px;"><img src="pic_mountain.jpg" alt="Mountain View" style="width:304px;height:228px;"><img src="pic_mountain.jpeg" alt="Mountain View" style="width:304px;height:228px;"></body></html>'
    h.feed(data)
    print(h.list)

    objects = list()
    values = list()
    for key, value in h.list.iteritems():
        objects.append(key)
        values.append(value)
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects, rotation='vertical')
    plt.ylabel('Usage')
    plt.title('Links usage')

    directory = 'links/'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    plt.savefig(directory + datetime.datetime.now().strftime("%d%m%Y%H%M%S%f") + '.png', bbox_inches='tight')
    plt.clf()