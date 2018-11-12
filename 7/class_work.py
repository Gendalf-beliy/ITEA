def number_gen():
    c = 0
    for i in range(1000):
        yield c + 1
        stop = (yield)
        if stop is not None:
            raise StopIteration


a = number_gen()
# a = (i for i in range(1000000))
for i in range(10):
    print(next(a))
a.send(2)
