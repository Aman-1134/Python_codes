num = list(range(1, 1000))
ctr = 0
for i in num:
    if str(i) == str(i)[::-1]:
        ctr += 1
        print('{}       {}' .format(int(i), ctr))
