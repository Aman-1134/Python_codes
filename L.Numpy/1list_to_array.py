import numpy as np

nlist = [1, 2, 3, 4]

narray = np.array(nlist)

print('List is ', nlist)
print('Array is', narray)

nlist = nlist + [5]             # scalar addn
print('Scalar addition occurs in list and result is ', nlist)
narray = narray + [5]           # does vector addn ie adds 5 to each elements in the array
print('Vector addition occurs in array and result is', narray)

print('Squaring an array', narray**2)                # square of each term in array

# np.sqrt(narray) or use log or exp





