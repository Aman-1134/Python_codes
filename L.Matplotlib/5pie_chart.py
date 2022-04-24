import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

classes = ['Python', 'Html', 'Java', 'C++', 'Ruby on Rails']
class1 = [30, 10, 25, 20, 15]

explode = [0, 0.04, 0, 0.04, 0.02]           # slices the parts in pie chart
color = ['r', 'g', 'b', 'c', 'm']
textproperty = {'fontsize': 15, 'color': 'k', 'fontstyle': 'italic'}
# wedge = {'linewidth': 4, 'width': 2, 'edgecolor': 'k'}   change width value and observe chart
wedge = {'linewidth': 2, 'edgecolor': 'k'}
# linewidth = boarder width
style.use('Solarize_Light2')

plt.pie(class1, labels=classes, explode=explode, colors=color, autopct='%0.2f%%', shadow=True, radius=1.5,
        startangle=90, textprops=textproperty, wedgeprops=wedge)

# use rotatelabels to rotate text around chart
# , center=(5,8), center of pie chart
# can use labeldistance for programmimg language and pctdistance for % shown
# autopct = auto percentage to show % value in each slice
plt.legend(loc='best', borderpad=2)
plt.show()

