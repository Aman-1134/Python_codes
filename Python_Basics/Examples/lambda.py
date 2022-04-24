sum_l = lambda a, b: a+b
print(sum_l(1, 2))

sum_l_args = lambda *args: sum(args)
print(sum_l_args(1, 2, 3, 4))

fact = lambda n: 1 if n == 1 else n*fact((n-1))
print(fact(5))
