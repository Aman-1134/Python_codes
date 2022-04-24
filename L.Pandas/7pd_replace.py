import pandas as pd
df = df = pd.read_csv('D:\\Excel Demo\\missing_value.csv', na_values=['not avaliable', 'no value'])
print(df)
print()

print('Replacing Distinction with Excellent:')
print(df.replace(to_replace='Distinction', value='Excellent'))     # same as print(df.replace('Distinction, 'Excellent')
print()

print(df.replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
print()

print('Replacing more than one value of more than one column:')
print(df.replace({'Division': 'Distinction', 'Name': 'Aman Ansari'}, 'Excellent'))
print()

print('Using regular expression to replace all the strings to int')
print(df.replace('[A-Za-z]', 10, regex=True))
print()

print('Replace strings of a column using dictionary:')
print(df.replace({'Division': '[A-Za-z]'}, 10, regex=True))
print()

print('Understanding ffill in replace with parameter limit:')
print(df.replace('First', method='ffill', limit=1, inplace=False))
print()

