def unpacker(args):
    new = [unpacker(x) for x in args]
    return new


# print(unpacker(([1,2,3],[4,5])))
print(unpacker((1, 2, 3, [4, 5], [6, 7, [8], [9]])))


