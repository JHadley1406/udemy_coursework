from rx import Observable


def print_value(value):
    print("{} is the value".format(value))


Observable.from_(['abc', 'def', 'ghi']).subscribe(print_value)

Observable.interval(1).take_until(Observable.timer(30)).sample(1).subscribe(print_value)
