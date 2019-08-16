from rx import Observable



def print_value(value):
    print("{} is the value.".format(value))


Observable.from_(['abc', 'def', 'ghi']).subscribe(print_value)


def say_hello(name, callback):
    callback('hello {}!'.format(name))


hello = Observable.from_callback(say_hello) # a factory to create new observables
hello('Rudolf').subscribe(print_value) # actually creates an observable
hello('observable').subscribe(print_value)

Observable.from_list([1, 2, 3]).subscribe(print_value)

Observable.of(1, 2, 3, 'A', 'B', 'C').subscribe(print_value)

from rx.testing import marbles, TestScheduler

test_scheduler = TestScheduler()

# Observable.from_marbles('--(a1)-(b2)---(c3)|', test_scheduler).subscribe(print_value)
# Observable.from_marbles('(a6)---(b5)(c4)|', test_scheduler).subscribe(print_value)

# test_scheduler.start()

# Observable.interval(10, test_scheduler).take_until(Observable.timer(30)).subscribe(print_value)

# test_scheduler.start()
print('__ Buffer')
Observable.from_(range(2000)).buffer(Observable.interval(10)).\
    subscribe(lambda buffer: print('# of items in buffer: {}'.format(len(buffer))))
print('__ Buffer with count')

Observable.from_(range(10)).buffer_with_count(3).subscribe(print_value)
print('__ Buffer with time')
Observable.interval(10, test_scheduler).take_until(Observable.timer(30)).buffer_with_time(20).subscribe(print_value)
test_scheduler.start()
