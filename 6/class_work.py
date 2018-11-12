import contextlib

with open('input.txt', 'r') as input:
    out = open('output.txt', 'w')
    with contextlib.redirect_stdout(out):
        for string in input:
            print(string, end='')


class context:

    def __init__(self, num):
        self.num = num
        self.count = 0

    def __enter__(self):

        for i in range(self.num * 101+1):
            if i % self.num == 0:
                count += 1
                yield i

    def __exit__(self):
        if self.count == 100:
            raise StopIteration


with context(17):
    print(1)
