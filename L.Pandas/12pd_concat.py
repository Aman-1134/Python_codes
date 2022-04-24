import pandas as pd

sr1 = pd.Series([1, 2, 3, 4, 5])

sr2 = pd.Series([6, 7, 8, 9, 10])

print('Concat two series')
sr_c = pd.concat([sr1, sr2])   # joins two series 1 and 2
print(sr_c)
print()

df1 = pd.DataFrame({'ID': [6, 7, 8, 9, 10],
                    'Name': ['Sajesh', 'Godar', 'Muskan', 'Lok', 'Dipesh'],
                    'Class': [8, 9, 10, 11, 12]})

df2 = pd.DataFrame({'ID': [1, 2, 3, 4, 5],
                    'Name': ['Aman', 'Vinay', 'Gopal', 'Amit', 'Hasina'],
                   'Class': [3, 4, 5, 6, 7]})

print('Concat two data frames row wise')
df_c = pd.concat([df2, df1], axis=1)    # unequal length data frames can also be concatenated and nan is placed in missing spaces
print(df_c)
print()

print('concat by ignoring the index of both dataframes')
df_c = pd.concat([df2, df1], axis=0, ignore_index=True, keys=['df2', 'df1'])
print(df_c)                         # keys give names at a side
print()

df3 = pd.DataFrame({'ID': [6, 7, 8, 9, 10],
                    'Name': ['Sajesh', 'Godar', 'Muskan', 'Lok', 'Dipesh'],
                    'Class': [8, 9, 10, 11, 12]})

df4 = pd.DataFrame({'ID': [1, 2],
                    'Name': ['Aman', 'Vinay'],
                   'Class': [3, 4]})

print('concat unequal data frames')
df_ec = pd.concat([df3, df4], axis=1, join='inner')     # concatenating unequal data frames
print(df_ec)                            # join= inner shows only similar index terms
print()                                 # join=outer  <default>

df5 = pd.DataFrame({'Marks': [20, 30, 40, 50]})

df = pd.concat([df1, df5], axis=1)
print(df)
