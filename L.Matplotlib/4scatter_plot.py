import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

df = pd.read_csv('D:\\Excel Demo\\Kaggle\\heart.csv')

style.use('Solarize_Light2')

x = df['trestbps']
y = df['chol']
plt.figure(figsize=(10, 7))
plt.grid(color='b', linewidth=0.5, linestyle=':')

plt.scatter(x, y, c='r', marker='.', s=200, alpha=0.5, linewidths=2, edgecolors='g',
            label='Cholesterol')
plt.scatter(x, df.age, c='y', marker='o', s=100, alpha=0.5, linewidths=2, edgecolors='b',
            label='Age')

# s = marker size, edge color = border color,

plt.title('Possibilities of heart attack', fontsize=30, color='r')
plt.xlabel('Threshold BP', color='m', fontsize=20)
plt.ylabel('Cholesterol and Age group', color='m', fontsize=20)
plt.legend()
plt.show()