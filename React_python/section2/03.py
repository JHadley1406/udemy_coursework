from rx import Observable
from rx.testing import marbles, TestScheduler

test_scheduler = TestScheduler()


def print_value(value):
    print("{} is the value.".format(value))


print('-- Group By')


def key_selector(x):
    if x % 2 == 0:
        return 'even'
    return 'odd'


def subscribe_group_observable(group_observable):
    def print_count(count):
        print('Group Observable Key "{}" contains {} items'.format(group_observable.key, count))

    group_observable.count().subscribe(print_count)


groups = Observable.from_(range(23)).group_by(key_selector)
groups.subscribe(subscribe_group_observable)

print('-- Sample')

Observable.interval(1, test_scheduler).take_until(Observable.timer(30)).sample(3).subscribe(print_value)
test_scheduler.start()


print('-- Max')
Observable.from_([1, 14, 2, 3, 4, 12, 3, 3, -10]).max(lambda x, y: x-y).subscribe(print_value)
