import threading


class FlightReservation:

    def __init__(self, ticket_left):
        self.L = threading.Semaphore()
        self.ticket_left = ticket_left

    def buy(self, ticket_requested):
        self.L.acquire()
        print("{0} is accessing buy()\n".format(threading.current_thread().getName()))
        if self.ticket_left >= ticket_requested:
            print("Your ticket is confirmed\n")
            print("Please make a payment and take your ticket\n")
            self.ticket_left -= ticket_requested
        else:
            print("There are not enough tickets remaining\n")
        print("{0} is exiting buy()\n".format(threading.current_thread().getName()))
        self.L.release()


myobj = FlightReservation(9)

t1 = threading.Thread(target=myobj.buy, args=[3])
t2 = threading.Thread(target=myobj.buy, args=[4])
t3 = threading.Thread(target=myobj.buy, args=[3])

t1.start()
t2.start()
t3.start()
