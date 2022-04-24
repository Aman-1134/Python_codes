import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

np.random.seed(20)
ml_st_age = np.random.randint(20, 45, (100))
py_st_age = np.random.randint(20, 45, (100))

bins = [20, 25, 30, 35, 40, 45]                # gives the range for bar diagram
plt.figure(figsize=(10, 7))                    # maintain this position for fig size syntax
                                               # figsize gives the aspect ratio

style.use('ggplot')
plt.grid(color='m', linewidth=0.5, linestyle=':')
plt.hist([ml_st_age, py_st_age], bins, color=['y', 'g'], rwidth=0.6, histtype='bar',
         orientation='vertical', label=['ML Students', 'PY Students'])            # rwidth gives the % of occupying(0-1)
plt.title('Machine Learning Student Age')
plt.xlabel('Age of Students')
plt.ylabel('Number of Students')
plt.legend()
plt.show()