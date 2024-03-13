#%%
import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(0, 0.5, 1000)
#plt.hist(values, 100)
#plt.show()

print('20 percentile: ' , str(np.percentile(values, 20)))
print('50 percentile: ' , str(np.percentile(values, 50)))
print('90 percentile: ' , str(np.percentile(values, 90)))