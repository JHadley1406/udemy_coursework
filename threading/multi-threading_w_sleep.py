import threading
from time import sleep


def natural_number():
    print(threading.current_thread().getName(), " Has Started")
    sleep(2)
    for x in range(10):
        print(x)

    print(threading.current_thread().getName(), " Has Ended")


t1 = threading.Thread(target=natural_number)
t2 = threading.Thread(target=natural_number)

t1.start()
t2.start()
