# Data frames are two dimensional series
import pandas as pd

list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4], [1, 2, 5, 7]]
df1 = pd.DataFrame(list1, index=['a', 'b', 'c', 'd'])
print('Data frame of 4*4 list')            # Data frame from a list
print(df1)
print()

dict1 = {'ID': [1, 4, 6, 9], 'Name': ['Aman', 'Rajesh', 'Karan', 'Vinay']}
df2 = pd.DataFrame(dict1, index=['a', 'b', 'c', 'd'])
print('Data frame of dictionary')          # Data frame from a dictionary
print(df2)
print()

l_of_dict = [{'a': 1, 'b': 2}, {'a': 4, 'b': 7, 'c': 6} ]
df3 = pd.DataFrame(l_of_dict)              # Data frame from list of dictionaries
print('Data frame of list of Dictionary')
print(df3)
print()

dict_ser = {'ID': pd.Series([1, 2, 3, 4]), 'Name': pd.Series(['Aman', 'Rajesh', 'Karan', 'Vinay'])}
df4 = pd.DataFrame(dict_ser)                # Data frame from dictionary series
print('Data frame of dictionary series')
print(df4)
