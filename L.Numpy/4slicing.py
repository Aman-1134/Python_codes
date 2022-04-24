import numpy as np

mx = np.arange(1, 101).reshape(10, 10)
print(mx)
print(mx[:, 0])                 # all elements in first column
print(mx[0])                    # all elements in first row


print(mx[1:4, 1:4])           # accessing certain members of the matrix mx

#concatinate arrays

arr1 = np.arange(1, 17).reshape(4, 4)
arr2 = np.arange(17, 33).reshape(4, 4)
print('First array arr1')
print(arr1)
print('Second array arr2 is')
print(arr2)
print()
print('Concetanated array of arr1 and arr2 column-wise')
print(np.concatenate((arr1, arr2)))          # column concatenation or use vstack
print()
print('Concetanated array of arr1 and arr2 row-wise')
print(np.concatenate((arr1, arr2), axis=1))  # row concatenation or use hstack

# x = np.split(arr2, 2)                       # colomn splitting
# print(type(np.split(arr1, 2)))
# print(x[0])
# print(type(x[0]))                           # <class 'numpy.ndarray'>

# x = np.split(arr1, 2, axis=1)               # row splitting
# print(x)
# x = np.split(arr1, [1,2], axis=1)

d1 = np.array([1, 3, 5, 4, 7, 9, 8, 6])
d2 = np.split(d1, [1, 4])
print(d2)