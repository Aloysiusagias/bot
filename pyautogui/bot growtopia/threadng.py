import threading
import time

def do_something():
    for i in range(20):
        time.sleep(1)
        print(i,"a")
        if(stopp):
            break
            

stopp = False
t1 = threading.Thread(target=do_something)
t1.start()

for i in range(20):
    time.sleep(0.25)

stopp = True