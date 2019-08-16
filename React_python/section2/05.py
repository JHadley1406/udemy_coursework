from rx import Observable
from rx.testing import TestScheduler


def print_value(x):
    print(x)


Observable.from_([1, 2, 3]).map(lambda x: x-1).subscribe(print_value)
Observable.from_([{'a': 1}, {'b': 2}, {'c': 3}]).map(lambda data: {**data, 'Hello': 'World'}).subscribe(print_value)

print('-- FlatMap')


def read_last_line_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        last_line = lines[-1]
        return Observable.just(last_line)


read_last_line_from_file('test.csv').flat_map(lambda line: read_last_line_from_file('test2.csv')).subscribe(print_value)


print('-- Window_with_count')

Observable.from_(range(3)).window_with_count(2).subscribe(print_value)


print('-- window_with_count.flat_map')
Observable.from_(range(3)).window_with_count(2).flat_map(lambda x: x).subscribe(print_value)

print('-- window_with_time')
wwt_test_scheduler = TestScheduler()

Observable.interval(50, wwt_test_scheduler).take_until(Observable.timer(100)).window_with_time(10).subscribe(
    lambda observable: observable.count().subscribe(print_value)
)

# test_scheduler.start()

print('-- Combine Latest')
cl_test_scheduler = TestScheduler()

Observable.combine_latest(
    Observable.interval(1, cl_test_scheduler).map(lambda x: 'a: {}'.format(x)),
    Observable.interval(2, cl_test_scheduler).map(lambda x: 'b: {}'.format(x)),
    lambda a, b: '{}; {}'.format(a, b)
).take_until(Observable.timer(1)).subscribe(print_value)
# cl_test_scheduler.start()


print('-- Zip')

zip_test_scheduler = TestScheduler()

Observable.zip(
    Observable.interval(1, zip_test_scheduler).map(lambda x: 'a: {}'.format(x)),
    Observable.interval(2, zip_test_scheduler).map(lambda x: 'b: {}'.format(x)),
    lambda a, b: '{}; {}'.format(a, b)
).take_until(Observable.timer(1)).subscribe(print_value)
zip_test_scheduler.start()
