import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3, 4],
                    'B': [10, 20, 30, 40]},
                   index=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame({'C': [5, 6, 7, 8],
                    'D': [50, 60, 70, 80]},
                   index=['a', 'b', 'c', 'd'])

print('Joining both data frames with common indexes')
print('See results for different index and size of data frames')
x = df1.join(df2)
print(x)

df3 = pd.DataFrame({'A': [5, 6, 7],
                    'B': [50, 60, 70]},
                   index=['a', 'b', 'c'])
print('Both have common head A')
y = df1.join(df3, how='inner', lsuffix='_1')
print(y)


# Append #

z = df1.append(df3, ignore_index=True)
print(z)

df4 = pd.DataFrame({'C': [5, 6, 7],
                    'B': [50, 60, 70]},
                   index=['a', 'b', 'c'])

m = df1.append(df4)
print(m)
