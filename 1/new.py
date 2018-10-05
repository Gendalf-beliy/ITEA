def func(str):
    lst = []
    for s in str:
        lst.append(ord(s))
    return tuple(lst)

print(func('hello'))


def test(tpl):
    str = ''
    for num in tpl:
        str += chr(num)
    return str

print(test(func('hello')))