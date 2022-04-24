import numpy as np

print(np.random.random((2, 3)))         # random elements between 0-1
print()

print(np.random.randint(1, 40, (2, 3, 3)))       # 3d array with terms 1-40 randomly

print('random seed elements')
np.random.seed(10)                               # prints a same random value every time u run
x = np.random.randint(1, 40, (2, 3, 3))
print(x)

# np.random.rand(3, 3) gives a 3*3 matrix with elements range 0-1
# np.random.randn(3, 3) gives 3*3 matrix with elements +ve and -ve

list1 = [1, 2, 3, 4, 5]
# for i in range(1,20):
#    print(np.random.choice(list1))

print(np.random.permutation(list1))
