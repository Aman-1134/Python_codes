import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

# arr_2d = np.linspace(1, 5, 12).reshape(4, 3)
# sns.heatmap(arr_2d)

cancer_data = load_breast_cancer()
plt.figure(figsize=(10, 7))

annotkws = {'fontstyle': 'italic', 'alpha': 0.6, 'rotation': 'horizontal'}
cbarkws = {'orientation': 'vertical', 'shrink': 1, 'extend': 'min', 'drawedges': True}
xlabel = ['Thresh BP', 'Cholesterol', 'Thalach']

heart_df = pd.read_csv('D:\\Excel Demo\\Kaggle\\heart.csv', nrows=10)

heart_df = heart_df.drop(columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'],
                         axis=1).set_index('age')
# heart_df.head(5)
# print(heart_df)

sns.heatmap(heart_df, vmin=120, vmax=300, cmap='coolwarm', annot=True, annot_kws=annotkws, linewidths=2,
            linecolor='b', cbar_kws=cbarkws, xticklabels=xlabel)
plt.ylabel('Age of heart disease person')

# vmin, vmax and cmap for toolbar range and color respectively
# annot to show values in chart
# linewidth gives margins between each boxes
# xticklabel=false to hide x labels
# cbar = false to hide color bar

plt.show()

sns.heatmap(heart_df.corr(), annot=True, linewidths=2, linecolor='k')
plt.title('Correlation heatmap')
print(heart_df.corr())
plt.show()


# cancerr_df = pd.DataFrame(np.c_[cancer_data['data'], cancer_data['target']],
#                          columns=np.append(cancer_data['feature_names'], ['target']))
# print(cancerr_df)