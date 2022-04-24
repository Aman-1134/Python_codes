def memorize(func):
    memory = {}
    def caller(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return caller


@memorize
def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(499))
