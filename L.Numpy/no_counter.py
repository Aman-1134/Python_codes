import numpy as np
string = "123456789876543234565671421890987"

for i in range(10):
    x = str(i)
    c = np.char.count(string, x)
    print('count of {} = {}'.format(i, c))
