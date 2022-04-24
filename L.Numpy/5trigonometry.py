import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.grid(color='r', linestyle=':', linewidth='0.5')
print(np.sin(180))
print(np.cos(90))

# x_sin = np.arange(0, 4*np.pi, 0.1)
x_sin = list(map(lambda x: x * np.pi/180, range(1, 361)))
y_sin = np.sin(x_sin)
y_cos = np.cos(x_sin)
y_tan = np.tan(x_sin)
# print(x_sin)
# print(y_sin)

plt.plot(x_sin, y_sin, label='Sine Function', color='b')
plt.plot(x_sin, y_cos, label='Cosine Function', color='g')
plt.legend()
plt.show()

# plt.show()
