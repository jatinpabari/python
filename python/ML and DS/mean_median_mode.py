#%%
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


incomes = np.random.normal(25000, 5000, 10000)
print('mean: ' + str(np.mean(incomes)))
print('median: ' + str(np.median(incomes)))
ages = np.random.randint(low=10, high=90, size=100)
print('mode: ' + str(stats.mode(ages)))

plt.hist(incomes, 50)
plt.show()