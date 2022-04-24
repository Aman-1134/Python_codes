import pandas as pd
df1 = pd.DataFrame({'ID': [1, 2, 3, 4, 6],
                    'Class': [8, 9, 10, 11, 12]},
                   index=['a', 'b', 'c', 'd', 'e'])

df2 = pd.DataFrame({'ID': [1, 2, 3, 4, 5],
                    'Name': ['Aman', 'Vinay', 'Gopal', 'Amit', 'Hasina']},
                   index=['a', 'b', 'c', 'd', 'e'])

print('Merging with ID on')
dfm = pd.merge(right=df1, left=df2, on='ID')             # dfm= pd.merge(df2, df1, on='ID')
print(dfm)                            # since 5 is missing in id, it is not printed
print()

print('Merging acc to left data frame ie df2')
dfm = pd.merge(df2, df1, on='ID', how='left')           # printed acc to df2, ie all elements of df2
print(dfm)                                              # if outer, all elments printed and nan is placed in missing places
                                                        # how=inner <by defaultprint()
print('Merging with indicator true')
dfm = pd.merge(df2, df1, on='ID', how='outer', indicator=True)
print(dfm)
print()


df3 = pd.DataFrame({'ID': [6, 7, 8, 9, 10],
                    'Class': [8, 9, 10, 11, 12]},
                   index=['a', 'b', 'c', 'd', 'e'])

df4 = pd.DataFrame({'ID': [1, 2, 3, 4, 5],
                    'Name': ['Aman', 'Vinay', 'Gopal', 'Amit', 'Hasina']},
                   index=['a', 'b', 'c', 'd', 'e'])

print('With Diff ID heads')
dfm = pd.merge(df3, df4, right_index=True, left_index=True)     # Gives ID_x and ID_y
print(dfm)                                            # use when ID of both dataframe is totally different
print()

print('Naming ID heads')
dfm = pd.merge(df2, df4, on='ID', suffixes=('_one', '_two'))                 # Name_x and Name_y is given by default when both merging data frames are same
print(dfm)

