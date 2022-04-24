# ****************** Line chart of temperature vs days of two cities*******************

import matplotlib.pyplot as plt
from matplotlib import style

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
kalaiya_temp = [20, 25, 20, 28, 34, 30, 25, 29, 35, 33, 19, 29, 28, 39, 37]
birgung_temp = [25, 35, 33, 42, 36, 39, 40, 32, 29, 28, 23, 36, 38, 40, 38]
plt.figure(figsize=(10, 7))

# plt.plot(days, temp, color='g', marker='o', linestyle='-.', linewidth=2, markersize=7)  # marker gives the points design
# above is same as below

style.use('ggplot')                                              # gives grid in the boxes
plt.grid(color='m', linewidth=0.5, linestyle=':')                # to give design to grids

plt.plot(days, kalaiya_temp, 'go-.', linewidth=1, markersize=7)
plt.plot(days, birgung_temp, 'ro-.', linewidth=1, markersize=7)
plt.axis([0, 20, 15, 45])                                        # giving the initial value for the axes
plt.title('Kalaiya and Birgunj Temperature in past 15 days', fontsize=15)    # Setting the heading of the graph
plt.xlabel('Days', fontsize=10)                                  # x axis plot is days number
plt.ylabel('Temperature', fontsize=10)                           # y axis plot is temperature
plt.legend(['Kalaiya', 'Birgunj'])                               # sets the name of line

# use loc for location of the name, loc takes int value
# name of line can be given as plt.plot(label= 'Temperature line')

plt.show()                                                       # is done to show the graph
