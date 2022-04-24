import pandas as pd
import numpy as np

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
# df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\test.csv')
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

num_var = df.select_dtypes(['int64', 'float64'])
miss_num_var = [var for var in num_var if num_var[var].isnull().sum() > 0]
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']
for cat_var, miss in zip(cat_vars, miss_num_var):
    for var_class in df[cat_var].unique():
        df.update(df[df.loc[:, cat_var] == var_class][miss].replace
              (np.nan, df[df.loc[:, cat_var] == var_class][miss].mean()))

cat_var = df.select_dtypes('O')
miss_cat_var = [var for var in cat_var if cat_var[var].isnull().sum() > 0]
for var in miss_cat_var:
    df.update(cat_var.fillna(cat_var[var].mode()[0]))

df = pd.get_dummies(df, drop_first=True)

X = df.drop(columns='SalePrice')
y = df['SalePrice']

# print(X.shape)
# print(y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)                     # for the columns value to fit in a line
# print(lr.coef_)                               # to get coefficients of each fit models
# print('Intercept is ', lr.intercept_)          # to get the intercept

# Predict value of Houses

# print(lr.predict(X_test[0, :]))
lr.predict(X_test)
# print(y_test)

print(f'Accuracy of Machine Learnng Algorithm is = {lr.score(X_test, y_test)*100}%')
# lr.score is actually R squared error that indicates goodness of fit

# Ridge and Lasso Regression
# from sklearn.linear_model import Ridge, Lasso
#
# rd = Ridge()
# rd.fit(X_train, y_train)
# print('Accuracy using Ridge Regression is ', rd.score(X_test, y_test)*100)
#
# ls = Lasso(alpha=3, max_iter=10000)
# ls.fit(X_train, y_train)
# print('Accuracy using Lasso Regression is ', ls.score(X_test, y_test))

# Root Mean Square Error
y_pred = lr.predict(X_test)
# print(y_pred)
# print(y_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'mse = {mse} rmse = {rmse}')

# R squared Regression analysis

from sklearn.metrics import r2_score
print('R squared regression analysis ', r2_score(y_test, y_pred))