import threading


class FlightReservation:
    L = threading.Lock()

    def __init__(self, ticket_left):
        self.ticket_left = ticket_left

    L.acquire()
    def buy(self, ticket_requested):
        print("{0} is accessing buy()".format(threading.current_thread().getName()))
        if self.ticket_left >= ticket_requested:
            print("Your ticket is confirmed\n")
            print("Please make a payment and take your ticket\n")
            self.ticket_left -= ticket_requested
        else:
            print("There are not enough tickets remaining\n")
        print("{0} is exiting buy()".format(threading.current_thread().getName()))
    L.release()


myobj = FlightReservation(9)

t1 = threading.Thread(target=myobj.buy, args=[3])
t2 = threading.Thread(target=myobj.buy, args=[4])
t3 = threading.Thread(target=myobj.buy, args=[3])

t1.start()
t2.start()
t3.start()
