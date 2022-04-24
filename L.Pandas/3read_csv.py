import pandas as pd

df = pd.read_csv('D:\Excel Demo\Student_results.csv')
print(df)
print()
# print(type(df))          #<class 'pandas.core.frame.DataFrame'>
# print(df.columns)          # Index(['Roll No', 'Name', 'Marks', 'Percentage', 'Division', 'Rank'], dtype='object')

df = pd.read_csv('D:\Excel Demo\Student_results.csv', nrows=5)   # nrows gives number of rows to print
print('Gives first five rows:')
print(df)
print()

df = pd.read_csv('D:\Excel Demo\Student_results.csv', usecols=[0, 1, 5])   # give index of columns to print
print('Prints columns mentioned in the list:')
print(df)
print()

# df = pd.read_csv('D:\Excel Demo\Student_results.csv', skiprows=1)   # if skip rows = 2, two rows are left
# print(df)            # to skip multiple rows skiprows =[0, 2]

df = pd.read_csv('D:\Excel Demo\Student_results.csv', index_col='Rank')
print('Rank column is made index:')
print(df)







