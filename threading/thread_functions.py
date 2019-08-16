import threading
from threading import Thread


def evenNumber():
    for x in range(20):
        if x%2 is 0:
            print(x)
    threading.current_thread().setName("even_number_thread")
    a = threading.current_thread().getName()
    print(a)


t = Thread(target=evenNumber)
t.start()



