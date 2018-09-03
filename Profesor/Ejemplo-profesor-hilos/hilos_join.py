import threading
import time

def printer_hello():
    for _ in range(3):
        time.sleep(1.0)
        print "hello"

def printer_mundo():
    for _ in range(3):
        time.sleep(1.0)
        print "mundo"
        
thread1 = threading.Thread(target=printer_hello)
thread2 = threading.Thread(target=printer_mundo)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print "goodbye"
