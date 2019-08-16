import threading


def even_number():
    print(threading.current_thread().getName())
    print("Even numbers are: ")
    for x in range(10):
        if x%2 is 0:
            print(x)


def odd_number():
    print(threading.current_thread().getName())
    print("Odd numbers are: ")
    for x in range(10):
        if x%2 is not 0:
            print(x)


def even_odd():
    print(threading.current_thread().getName())
    even_number()
    odd_number()


t = threading.Thread(target=even_odd, name="Even_Odd_Thread")
t.start()
