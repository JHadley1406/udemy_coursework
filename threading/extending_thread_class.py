import threading


class MyThread(threading.Thread):

    # MUST override run method
    def run(self):
        print(threading.current_thread().getName())
        print("Egyptian Pyramid")
        for x in range(0, 5):
            for j in range(0,x+1):
                print("*", end=" ")
            print("\n")


pyramid = MyThread(name="Pyramid Thread")

pyramid.start()


