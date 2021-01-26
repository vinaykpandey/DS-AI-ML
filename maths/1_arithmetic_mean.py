from functools import reduce


def avg(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


def Avg(lst):
    n = len(lst)
    sum_num = 0
    for num in lst:
        sum_num = sum_num + num
    return sum_num / n
