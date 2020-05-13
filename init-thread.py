import threading
import time

def sleeper(n):
    print(f"Hi I'll sleep for {n} seconds")
    time.sleep(n)
    print("I have awakened!")

t = threading.Thread(target = sleeper, name = "test-thread", args = ([5]))
t.start()

print("Wake up")
