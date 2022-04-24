from functools import reduce

out = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5, 6])
print(out)


def fact(n):
    product = reduce(lambda x, y: x*y, range(1, n+1))
    return product


print(fact(5))

maximum = reduce(lambda x, y: x if x > y else y, [1, 44, 23, 55, 46, 34, 74, 22, 39])
print(maximum)
