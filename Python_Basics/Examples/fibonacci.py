t1 = 1
t2 = 2
terms = int(input('Enter the number of Terms::'))

if terms == 1:
    print(t1)
elif terms == 2:
    print(t1, end=' ')
    print(t2, end=' ')
else:

    print(t1, end=' ')
    print(t2, end=' ')
    for i in range(2, terms):
        x = t1
        t1 = t2
        t2 = x + t2

        print(t2, end=' ')

