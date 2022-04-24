import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

df = pd.DataFrame(np.c_[data.data, data.target], columns=[list(data.feature_names) + ['target']])

X = df.iloc[:, 0: -1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)

# Train Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, criterion='gini')
classifier.fit(X_train, y_train)
print(classifier.score(X_test, y_test))

# Predict Cancer
patient1 = [2.65231762,  1.77811311,  2.60622732,  2.96324283, -0.06609518,  1.2865035,
  1.39134077,  2.02614144,  0.42575834,  0.06852025,  2.34529764, -0.45881107,
  2.12990317,  2.49940587, -0.22502254,  0.20659226,  0.40832774,  0.84422126,
 -0.53992908, -0.25877397,  3.13514068,  1.44385864,  3.02114476,  3.71998397,
  0.68780346,  1.1121591,   1.58152563,  2.28828386,  0.3734377,   0.20303736]

# print(patient1)

patient1 = np.array(patient1).reshape(1, 30)
pred = classifier.predict(patient1)
if pred[0] == 0:
    print('Patient has Cancer (Malignant)')
else:
    print('Bening Symptoms')
# Save Model
import pickle
pickle.dump(classifier, open('Classifier_pickle', 'wb'))
# pickle.dump(model_name, open('file_location', 'wb'))
model = pickle.load(open('Classifier_pickle', 'rb'))
print(model.predict([X_test.iloc[-1, :]]))

import joblib
joblib.dump(classifier, 'Classifier_jlb')
model2 = joblib.load('Classifier_jlb')
print(model2.predict([X_test.iloc[-1, :]]))
