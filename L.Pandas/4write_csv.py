import pandas as pd

df = pd.read_csv('D:\Excel Demo\Student_results.csv')
print(df)
print()
# df = pd.read_csv('D:\Excel Demo\Student_results.csv', header=[2]) # changes the label<header> to row with index 2
# print(df)         if header = none, index is printed as header starting from 0

df1 = pd.read_csv('D:\Excel Demo\Student_results.csv', header=None, prefix='Columns')  # always used with header=None
print(df1)
print()

df2 = pd.read_csv('D:\Excel Demo\Student_results.csv', names=['a', 'b', 'c', 'd', 'e', 'f'])  # gives a header as mentioned in the list
print('Header as alphabets:')
print(df2)
print()

print('First four rows:')
print(df.head(4))         # if int not mentioned first 5 rows are printed
print()

# use print(df.tail()) to print bottom value

df4 = pd.read_csv('D:\Excel Demo\Student_results.csv', dtype={'Percentage': 'float64', 'Marks': 'float64'})
print('Changing percentage and marks to default float:')
print(df4)
print()

df5 = pd.read_csv('D:\Excel Demo\Student_results.csv', true_values=['Distinction'], false_values=['First'])
print(df5)
