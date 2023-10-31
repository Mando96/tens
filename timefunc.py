import time
from threading import Thread

answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print("Too Slow")

    

Thread(target = check).start()

answer = input("Input something: ")

#Timer func
time_limit = 5
start_time = time.time()
print (start_time)
''
time_elapsed = time.time() - start_time
print (time_elapsed)
