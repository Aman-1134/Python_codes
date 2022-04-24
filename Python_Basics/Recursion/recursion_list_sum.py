def add(num):
    print(num)
    if len(num) == 1:
        return num
    else:
        num[0] = num[0] + num[-1]
        return add(num[:-1])

lon = [1,2,6,4,5,3,7,9,8,10]
y=add(lon)
print(y[0])