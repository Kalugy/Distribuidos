from __future__ import print_function
import psutil
print("cpu: " , psutil.cpu_percent())

print("memoria ", psutil.virtual_memory()) #  physical memory 

