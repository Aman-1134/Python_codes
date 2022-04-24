import os

#f = open('test.txt','a')
with open('test.txt', 'w+') as f:
    print(f.writelines(['Hello world']))
    print(f.closed)

#f.close()
#print(f.close)
