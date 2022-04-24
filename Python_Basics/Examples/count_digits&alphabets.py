string = "I am Don of Advanced College 2020"
a = d = o = s = 0
for i in string:
    if i.isalpha():
        a = a+1
    elif i.isdigit():
        d = d+1
    elif i == ' ':
        s = s+1
    else:
        o = o+1
print('alphabets = {} , numbers = {} , others = {} , spaces = {}'.format(a, d, o, s))
