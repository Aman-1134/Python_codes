import time
def time_calc(fn, *args):
    start = time.time()
    fn(*args)
    end = time.time()
    return end - start

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def print_name(fname, lname):
    print(fname, lname)

print(time_calc(fibo, 34))
print(time_calc(print_name, 'aman', 'ansari'))

print(fibo(34))
print(print_name('aman', 'ansari'))
