# thread test

import threading
import time

def say(msg):
    for i in range(100):
        print(msg)
        time.sleep(1)

thread_1 = threading.Thread(target=say, args=("you ",))
time.sleep(0.1)
thread_2 = threading.Thread(target=say, args=("need ",))
time.sleep(0.1)
thread_3 = threading.Thread(target=say, args=("python",))
time.sleep(0.1)

if __name__ == "__main__":
    thread_1.start()
    thread_2.start()
    thread_3.start()

    for i in range(100):
        print(i)
        time.sleep(0.1)