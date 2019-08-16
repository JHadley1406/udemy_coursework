class Addition:
    def __init__(self, *args):
        if len(args) == 0:
            self.numbers = (0,0)
        else:
            self.numbers = args

    def __add__(self, other):
        sum = tuple(x + y for x,y in zip(self.numbers, other.numbers))
        return Addition(*sum)


obj1 = Addition(2,3)
obj2 = Addition(4,5)
obj3 = obj1 + obj2

print(obj3.numbers)

