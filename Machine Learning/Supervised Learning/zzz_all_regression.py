import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(25, 25))
data = pd.read_csv("D:\Excel Demo\Kaggle\House Price\\train.csv")
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

data_num = data.select_dtypes(['int64', 'float64'])

data_num_miss = [var for var in data_num if data_num[var].isnull().sum() > 0]
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']

for cat, miss in zip(cat_vars, data_num_miss):
    for var in data[cat].unique():
        data.update(data[data.loc[:, cat] == var][miss].replace
                    (np.nan, data[data.loc[:, cat] == var][miss].mean()))

# print(data.select_dtypes(['int64', 'float64']).isnull().sum().sum())

data_obj = data.select_dtypes('O')
data_b = [var for var in data_obj if data_obj[var].isnull().sum()/data.shape[0]*100 > 20]
data = data.drop(columns=data_b)
data_obj = data.select_dtypes('O')
data_obj_miss = [var for var in data_obj if data_obj[var].isnull().sum() > 0]

for miss in data_obj_miss:
    data.update(data_obj.fillna(data_obj[miss].mode()[0]))

data1 = data.select_dtypes('O')
data = pd.get_dummies(data)

X = data.drop(columns='SalePrice')
y = data['SalePrice']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

from sklearn.tree import DecisionTreeRegressor
dr = DecisionTreeRegressor()
dr.fit(X_train, y_train)
print('Decision Tree Accuracy = ', dr.score(X_test, y_test))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
print('Linear Regression Accuracy = ', lr.score(X_test, y_test))

from sklearn.svm import SVR
svr = SVR()
svr.fit(X_train, y_train)
print('Support Vector Regressor Accuracy = ', svr.score(X_test, y_test))


from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2)
pf.fit(X_train)
X_train_p = pf.transform(X_train)
X_test_p = pf.transform(X_test)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train_p, y_train)
print('Polynomial Regression Accuracy = ', lr.score(X_test_p, y_test))
print('Accuracy = ', float(lr.score(X_train_p, y_train)))
# y_pred = lr.predict(X_test_p)
# print(y_pred)
# print(y_test)
