import pandas as pd

df = pd.read_csv('D:\Excel Demo\interpolate_it.csv', parse_dates=['Date'], index_col='Date')
print(df)

print('Interpolated data frame with linear method:')
print(df.interpolate())     # default method = linear

#print(df.interpolate('time'))

print('Interpolate acc to index Date:')
print(df.interpolate(method='index'))          # Before interpolation none elements in index column should be nan
# if polynomial method is used order of polynomial has to be mentioned

# if u use axis none row or column should be object type. If possible maintain same data type for all

print(df.interpolate(limit=1, limit_direction='backward'))      # if dirn not mentioned default is forward
# direction can also be set to both
print()

print('Exterpolate:')
print(df.interpolate(limit_area='outside'))      # Exterpolate if area =  inside, interpolate

