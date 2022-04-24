import numpy as np

str1 = 'Learning Python '
str2 = 'In Pycharm'

print(np.char.add(str1, str2))
print(np.char.lower(str1))
print(np.char.upper(str2))

print(np.char.center(str1, 60))
print(np.char.center(str1, 60, fillchar='*'))
print()
print('splitting')
print(np.char.split(str2))

str3 = 'dmy'
str4 = 'dmy'
print(np.char.join([':', '/'], [str3, str4]))

print(np.char.replace(str1, 'Python', 'Java'))

# print(np.char.equal(str3, str4))
# print(np.char.count(str1, 'a'))
# print(np.char.find(str1, 'P'))
