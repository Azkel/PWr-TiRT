#!/usr/bin/python

import receiver
import frame_filter

while 1:
    data = receiver.listen()
    print 'Received frames:', len(data)
    print 'Filtering TCP/IP frames...'
    data = frame_filter.filter_frames(data)
    print 'After filtering there are ', len(data), ' left.'