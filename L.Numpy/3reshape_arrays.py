import numpy as np

arr = np.zeros((2, 3))           # np.zeros((2, 3), dtype=np.int16) to get integer elements <can use np.ones() or np.empty()
print(arr)

print(np.arange(1, 8))           # array having elements 1-7
print()
print(np.linspace(1, 5, 10))            # if 10 not given 50 values are printed


m = arr.reshape(6, 1)
print(m)
print()

#a = np.ones((10, 1))
#b = a.reshape(5, -1)             # sets to 5*2 order
#print(a)
#print(b)

x = np.ones((1, 3))

y = np.vstack((arr, x))           # hstack to stack in horizontal dirn
print(y)                          # hsplit and vspit are there to slice matrices <arrays>


print()
a_1d = np.arange(1, 13)
print(a_1d)
print()
a_3d = a_1d.reshape(2, 3, 2)
print(a_3d)

print(a_3d.ravel())              # multi dimensional array to 1d or use a_3d.flatten()

# suppose a and b are 2 matrices then to multiply them use 'a @ b' or 'a.dot(b)'

