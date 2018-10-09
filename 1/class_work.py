import random

def ord_tuple(word):
    """
    Function get string and return tuple of every letter's ascii cod
    :param word: string
    :return: tuple of int
    >>> ord_tuple('Hello')
    (72, 101, 108, 108, 111)
    """
    lst = []
    for s in word:
        lst.append(ord(s))
    return tuple(lst)


def test_ord_tuple(tpl):
    """
    Function that tests ord_tuple function
    :param tpl:
    :return: bool
    >>> test_ord_tuple((72, 101, 108, 108, 111))
    True
    """
    str = ''
    for num in tpl:
        str += chr(num)
    return ord_tuple(str) == tpl


def lower_upper(x):
    """
    Function get number x and return dict with 50 random values between 0 and 1 - lower or upper of this number
    :param x: float
    :return: dict
    >>> dc = lower_upper(0.5)
    >>> all([x < 0.5 for x in dc['lower']]) and all([x > 0.5 for x in dc['upper']])
    True
    >>> len(dc['lower']) + len(dc['upper']) <= 50
    True
    """
    if 0 <= x <= 1:
        dc = {'lower': [], 'upper': []}
        for _ in range(50):
            num = random.random()
            if num < x:
                dc['lower'].append(num)
            elif num > x:
                dc['upper'].append(num)
        return dc
    else:
        print('x shoild be number in range [0, 1]')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
