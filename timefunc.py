import time

#count up
'''
running = True
seconds = 0
end = 10

while running:
    print(seconds)
    time.sleep(1)
    seconds +=1
    if seconds >= end :
        running = False
        print(seconds)
print("Done")

'''
#count down

'''
running = True
seconds = 10
end = 0

while running:
    print(seconds)
    time.sleep(1)
    seconds -=1
    if seconds <= end :
        running = False
        print(seconds)
print("Game Over")
'''
'''
#Python countdown timer
def countdown(time_sec): 
    while time_sec: 
        mins, secs = divmod(time_sec, 60) 
        timeformat = '{:02d}:{:02d}'.format(mins,secs) 
        print(timeformat,end='\r') 
        time.sleep(1) 
        time_sec -= 1

    print("Timer Ended!")

countdown(10) 
'''


time_limit = 5
start_time = time.time()

elapsed_time = time.time() - start_time
print(time_limit - int(elapsed_time))
if elapsed_time > time_limit:
    print ("Game Over")
    exit()