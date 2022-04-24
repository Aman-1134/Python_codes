import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('D:\Excel Demo\Kaggle\Bengaluru House Price\\Bengaluru_House_Data.csv', nrows=1000,
                 usecols=[0, 1, 3, 6, 7, 8])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

y = df['price']
df = df.drop(columns='price')
df_num = df.select_dtypes(['int64', 'float64'])

df.update(df_num.fillna(df_num['bath'].median()))
df.update(df_num.fillna(df_num['balcony'].mean()))

df_cat = df.select_dtypes('O')

area_map = {'Super built-up  Area': 4, 'Plot  Area': 3, 'Built-up  Area': 2, 'Carpet  Area': 1}
df['area_type'] = df['area_type'].map(area_map)

for var in df_cat:
    df.update(df_cat.fillna(df_cat[var].mode()[0]))

size_map = {'2 BHK': 2, '4 Bedroom': 2, '3 BHK': 3, '4 BHK': 4, '6 Bedroom': 3, '3 Bedroom': 1.5,
            '1 BHK': 1, '1 RK': 1, '1 Bedroom': 0.5, '8 Bedroom': 4, '2 Bedroom': 1, '7 Bedroom': 3.5,
            '5 BHK': 5, '7 BHK': 7, '6 BHK': 6, '5 Bedroom': 2.5, '11 BHK': 11, '9 BHK': 9,
            '1200': 3, '9 Bedroom': 4.5}
df['size'] = df['size'].map(size_map)
df.update(df['size'])
print(df['size'])
df.update(df_cat.replace(to_replace=['19-Dec', 'Ready To Move', '18-May', '18-Feb', '18-Nov', '20-Dec',
                                     '17-Oct',
 '21-Dec', '19-Sep', '20-Sep', '18-Mar', '20-Feb', '18-Apr', '20-Aug', '18-Oct',
 '19-Mar', '17-Sep', '18-Dec', '17-Aug', '19-Apr', '18-Jun', '22-Dec', '22-Jan',
 '18-Aug', '19-Jan', '17-Jul', '18-Jul', '21-Jun', '20-May', '19-Aug', '18-Sep',
 '17-May', '17-Jun', '21-May', '18-Jan', '20-Mar', '17-Dec', '16-Mar', '19-Jun',
 '22-Jun', '19-Jul', '21-Feb', 'Immediate Possession', '19-May', '17-Nov',
 '20-Oct', '20-Jun', '19-Feb', '21-Oct', '21-Jan', '17-Mar'], value=1))



print(df)


