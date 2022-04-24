import pandas as pd
import numpy as np

df = pd.read_csv('D:\Excel Demo\Kaggle\Bengaluru House Price\\Bengaluru Clean Data.csv')

# Split Data
X = df.drop(columns='price')
y = df['price']

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# SVR
from sklearn.svm import SVR
# svr_rbf = SVR()
# svr_rbf.fit(X_train, y_train)
# print(svr_rbf.score(X_test, y_test))       # accuracy = 0.2063803584082815

svr_linear = SVR(kernel='linear')           # if u use polynomial kernel mention its degree(default = 3)
svr_linear.fit(X_train, y_train)
print(svr_linear.score(X_test, y_test))

# Predict value of houses
y_pred = svr_linear.predict(X_test)
print(y_pred)
print(y_test)

# Root mean square errors
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'mse = {mse} rmse = {rmse}')