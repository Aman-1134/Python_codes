import pandas as pd
import numpy as np

df = pd.read_csv('D:\Excel Demo\Kaggle\Bengaluru House Price\\Bengaluru Clean Data.csv')

# Split Data
X = df.drop(columns='price')
y = df['price']

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

print('Training')
# Train Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, criterion='mse')
regressor.fit(X_train, y_train)
print(regressor.score(X_test, y_test))

# Prediction using trained model

# print(regressor.predict([X_test.iloc[-1, :]]))
# print(y_test.iloc[-1])

pred = regressor.predict(X_test)
print(pred)
print(y_test)