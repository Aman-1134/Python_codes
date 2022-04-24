import numpy as np

a = np.array([1, 2, 3, 4])

b = np.array([[1, 2], [3, 4], [5, 6]])
print('Accesing single member of the array', b[2][1])
print('Accesing single member of the array', b[2, 1])

b[2, 1] = 10
print('After changing one of the term in the 2D array ')
print(b)
print()

# M = np.matrix([[1, 2], [3, 4], [5, 6]])
# print(M)
# print()

transpose_b = b.T
print('Transpose of matrix b is ')
print(transpose_b)
print()

print('Shape of b ')
print(b.shape)             # gives the order of matrix
print(transpose_b.shape)

print('Dimention of a and b ')
print(a.ndim)         # n.dim gives dimention of array
print(b.ndim)

# b.size gives no of elements in array
# u can use np.min(), np.max(), np.sum(), np.mean(), np.log(), np.sqrt(), np.exp()

print(b.sum(axis=0))      # verticle sum of array elements (i.e. column)
                          # if axis = 1 horizontal sum is given ( i.e. row)

print(b.max(axis= 0))       # max in verticle axis

print(np.mean(b))
