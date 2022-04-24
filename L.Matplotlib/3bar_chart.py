import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

classes = ['Python', 'Html', 'Java', 'C++', 'Ruby on Rails']
class1 = [30, 10, 25, 20, 15]
class2 = [40, 30, 30, 25, 35]
class3 = [25, 40, 35, 30, 20]

style.use('Solarize_Light2')
# print(style.available)

plt.figure(figsize=(10, 7))
plt.grid(color='k', linewidth=0.5, linestyle=':')
class_index = np.arange(len(classes))          # gives [0 1 2 3 4] ie index of each language
width = 0.2

# plt.bar(classes, class1, color='g', width=0.5, align='center', edgecolor='r', linewidth=1, alpha=0.8,
 #       linestyle='--', label='Class1', visible=True)
# width is for width of bars n line width is for width of border of bars
# alpha maintains the opacity of bars(0-1), visible=False, the bars wouldn't show

plt.bar(class_index, class1, color='g', width=width,  label='Class1')
plt.bar(class_index + width, class2, color='y', width=width, label='Class2')
plt.bar(class_index + 2 * width, class3, color='b', width=width, label='Class3')

plt.xticks(class_index + width, classes, rotation=10)    # np.arange gives index of elements which is converted to their respective values ie class names
# rotation rotates the texts in classes by certain degree

plt.title('Programming Language and their students no')
plt.xlabel('Programming Language Classes', color='m')
plt.ylabel('Number of Students', color='m')
plt.legend()
plt.show()