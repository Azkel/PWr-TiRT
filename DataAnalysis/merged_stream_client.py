#Merged stream client
#Extract HTML code

import Pyro4
 
url = "PYRO:merged_stream@156.17.224.185:22222"
merged_stream = Pyro4.Proxy(url)

print("Received stream name:" +  merged_stream.getName())
