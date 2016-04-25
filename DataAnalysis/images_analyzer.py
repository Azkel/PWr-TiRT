#from html.parser import HTMLParser
from HTMLParser import HTMLParser
import os.path
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime


class MyParse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list = dict()

    def handle_starttag(self, tag, attrs):
        if tag=="img":
            extension = os.path.splitext(dict(attrs)["src"])[1]
            if extension in self.list:
                self.list[extension] += 1
            else:
                self.list[extension] = 1


def analyze(data):
    h=MyParse()
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
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Images extensions')

    plt.savefig('images/' + datetime.datetime.now().strftime("%d%m%Y%H%M%S%f") + '.png', bbox_inches='tight')
    plt.clf()