
while True:
    s = input()
    dc = {}
    if s == '':
        break
    else:
        x = s.split('=')
        dc[x[0]] = x[1]

a = type('name_of_class', (), dc)
b = a()
print(b)