num = list(range(1, 40))
print(num)
lob = []

for i in num:
    if i % 3 == 0 and i % 5 == 0:
        lob.append("FizzBuzz")
    elif i % 3 == 0:
        lob.append("fizz")
    elif i % 5 == 0:
        lob.append("buzz")
    else:
        lob.append(i)

print(lob)
