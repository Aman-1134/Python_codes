
#plt.savefig("Pie_Chart", dpi=1000, quality=99, facecolor='g', edgecolor='r')           # default file extension is png
# dpi =  dots per inch, face color gives the background color

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

plt.figure(figsize=(10, 7))

plt.subplot(3, 2, 1)

# ---------------------- Pie Chart ------------------------- #
classes = ['Python', 'Html', 'Java', 'C++', 'Ruby on Rails']
class1 = [30, 10, 25, 20, 15]
explode = [0, 0.04, 0, 0.04, 0.02]           # slices the parts in pie chart
color = ['r', 'g', 'b', 'c', 'm']
textproperty = {'fontsize': 8, 'color': 'k', 'fontstyle': 'italic'}
wedge = {'linewidth': 1, 'edgecolor': 'k'}
style.use('Solarize_Light2')

plt.pie(class1, labels=classes, explode=explode, colors=color, autopct='%0.2f%%', shadow=True, radius=1,
        startangle=90, textprops=textproperty, wedgeprops=wedge)

plt.subplot(3, 2, 2)

# ---------------------- Scatter plot ------------------- #
df = pd.read_csv('D:\\Excel Demo\\Kaggle\\heart.csv')

style.use('Solarize_Light2')

x = df['trestbps']
y = df['chol']

plt.scatter(x, y, c='r', marker='.', s=10, alpha=0.5, label='Cholesterol')
plt.scatter(x, df.age, c='y', marker='o', s=10, alpha=0.5, edgecolors='b', label='Age')
plt.title('Possibilities of heart attack', fontsize=7, color='r')
plt.xlabel('Threshold BP', color='m', fontsize=6)
plt.ylabel('Cholesterol and Age roup', color='m', fontsize=6)

plt.subplot(3, 2, 3)

# ------------------------------- Bar Chart ---------------------- #
classes = ['Python', 'Html', 'Java', 'C++', 'Ruby on Rails']
class1 = [30, 10, 25, 20, 15]
class2 = [40, 30, 30, 25, 35]
class3 = [25, 40, 35, 30, 20]

style.use('Solarize_Light2')
plt.grid(color='b', linewidth=0.5, linestyle=':')
class_index = np.arange(len(classes))          # gives [0 1 2 3 4] ie index of each language
width = 0.2

plt.bar(class_index, class1, color='g', width=width, label='Class1')
plt.bar(class_index + width, class2, color='y', width=width, label='Class2')
plt.bar(class_index + 2 * width, class3, color='b', width=width, label='Class3')

plt.xticks(class_index + width, classes, rotation=10)

plt.title('Programming Language and their students no', fontsize=7)
plt.xlabel('Programming Language Classes', color='m', fontsize=6)
plt.ylabel('Number of Students', color='m', fontsize=6)

plt.subplot(3, 2, 4)

# -------------------------- Line Chart ----------------------- #
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
kalaiya_temp = [20, 25, 20, 28, 34, 30, 25, 29, 35, 33, 19, 29, 28, 39, 37]
birgung_temp = [25, 35, 33, 42, 36, 39, 40, 32, 29, 28, 23, 36, 38, 40, 38]
style.use('ggplot')                                             # gives grid in the boxes
plt.plot(days, kalaiya_temp, 'go-.', linewidth=1, markersize=3)
plt.plot(days, birgung_temp, 'ro-.', linewidth=1, markersize=3)
plt.axis([0, 20, 15, 45])
plt.title('Kalaiya Temperature in past 15 days', fontsize=7)
plt.xlabel('Days', fontsize=6)
plt.ylabel('Temperature', fontsize=6)
plt.legend(['Kalaiya', 'Birgunj'], loc='lower right')
plt.grid(color='m', linewidth=0.5, linestyle=':')

plt.subplot(3, 2, 5)


np.random.seed(20)
ml_st_age = np.random.randint(20, 45, (100))
py_st_age = np.random.randint(15, 35, (100))

bins = [20, 25, 30, 35, 40, 45]

style.use('ggplot')
plt.grid(color='m', linewidth=0.5, linestyle=':')
plt.hist([ml_st_age, py_st_age], bins, color=['y', 'g'], rwidth=0.6, histtype='bar',
         orientation='vertical', label=['ML Students', 'PY Students'])
plt.title('Machine Learning Student Age', fontsize=7)
plt.xlabel('Age of Students', fontsize=6)
plt.ylabel('Number of Students', fontsize=6)
plt.legend()

plt.subplot(3, 2, 6, projection='polar', facecolor='k')
plt.savefig("Pie_Chart", dpi=1000, facecolor='m')
plt.show()