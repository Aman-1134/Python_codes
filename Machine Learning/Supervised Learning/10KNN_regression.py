import pandas as pd
import numpy as np

df = pd.read_csv('D:\Excel Demo\Kaggle\Bengaluru House Price\\Bengaluru Clean Data.csv')

# Split Data
X = df.drop(columns='price')
y = df['price']

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

# K Nearest Neighbour Regression

from sklearn.neighbors import KNeighborsRegressor
kr = KNeighborsRegressor()
kr.fit(X_train, y_train)
print(kr.score(X_test, y_test))

# Predict Prices
pred = kr.predict(X_test)
print(pred)
print(y_test)
