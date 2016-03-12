#Combined stream server
#Merge all streams and share it...

import time
import Pyro4
import sys
import mymodule

class MergedStream:

   def __init__(self, name):
      self.name = name  
    
   def getName(self):
      return self.name;

if __name__ == '__main__':
    Pyro4.config.SERIALIZER = "pickle"
    port_id = 22222  
    host = "192.168.1.109"
    merged_stream = MergedStream("test stream name")
    print('System started at port '+str(port_id)+'!')
    Pyro4.Daemon.serveSimple(
            {
                merged_stream: "merged_stream"
            },
            host = host,
            port = port_id,
            ns = False)
    while 1:
        time.sleep(0.1)
