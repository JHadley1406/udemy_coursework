import threading

class MyThread:
    def natural_number(self):
        if threading.current_thread().getName() == "Thread-1":
            for x in range(10):
                print(x)
        else:
            print(threading.current_thread().getName())



myObj = MyThread()
t = threading.Thread(target=myObj.natural_number)
t.start()
