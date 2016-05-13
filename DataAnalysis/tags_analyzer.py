#from html.parser import HTMLParser
from HTMLParser import HTMLParser
import os.path
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime


class TagsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list = dict()

    def handle_starttag(self, tag, attrs):
        try:
            unicode_tag = tag.decode("utf-8")
            if unicode_tag in self.list:
                self.list[unicode_tag] += 1
            else:
                self.list[unicode_tag] = 1

        except UnicodeDecodeError:
            pass



def analyze(data):
    h=TagsParser()
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
    plt.title('Tags usage')

    directory = 'tags/'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    plt.savefig(directory + datetime.datetime.now().strftime("%d%m%Y%H%M%S%f") + '.png', bbox_inches='tight')
    plt.clf()