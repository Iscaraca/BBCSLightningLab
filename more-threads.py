import threading
import time

def sleeper(n):
    print(f"Hi I'll sleep for {n} seconds")
    time.sleep(n)
    print("I have awakened!")

start = time.time()
threads = []

for i in range(5):
    t = threading.Thread(target = sleeper, name = 'thread{}'.format(i), args =([5]))
    threads.append(t)
    t.start()
    print('{} has started \n'.format(t.name))
 
 
 
    
for i in threads:

    i.join()
    
end = time.time()



print('time is {}'.format(end - start))
