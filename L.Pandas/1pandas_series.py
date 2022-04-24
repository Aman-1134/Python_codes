# series = label with its members(index). eg. students(label) and names of students is index
import pandas as pd

list1 = [1, 2, 4.5, 'aman']
series1 = pd.Series(list1)
print('series of list')
print(series1)
print()

#print(type(series1))         # <class 'pandas.core.series.Series'>
series2 = pd.Series([1, 23, 3.5, 5.34], index=['a', 'b', 'c', 'd'], dtype=float, name='datavalues')
print('series of list with index as in index list:')
print(series2)
print()

scalar_s = pd.Series(0.5, [1, 2, 3, 4])         # no matter if u write index=[1, 2, 3, 4]
print('index with common element 0.5:')
print(scalar_s)
print()
dict_s = pd.Series({'a': 1, 'b': 2})
print('Dictionary series:')
print(dict_s)
print()

series3 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print('values at index c is:')
print(series3['c'])          # accesing values in series according to index or use print(series3[3])
print()
print('values from index a-c:')
print(series3['a':'c'])

# use max(series3), min(series3) etc
print('series value greater than 2')
print(series3[series3 > 2])
print()

series4 = pd.Series([1, 3, 2, 5], index=['a', 'b', 'c', 'd'])
x = series3 + series4
print('addition of two series:')
print('Datas of same index are added:')
print(x)                   # adds elements of same index

# can use multiply, divide or subtract
series5 = pd.Series([1, 3, 2, 5, 8], index=['a', 'b', 'c', 'd', 'e'])    # has an extra element than series4
x = series4 + series5
print('Adds two series of unequal index:')
print(x)                   # adds elements of same index

# output NaN = not a number
# pandas also handles missing values effectively than excel
# a     2.0
# b     6.0
# c     4.0
# d    10.0
# e     NaN
# dtype: float64
