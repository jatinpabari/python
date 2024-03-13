#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

values = np.random.normal(0, 0.5, 1000)
#plt.hist(values, 100)
#plt.show()

#first moment - mean
print(np.mean(values))

#second moment - variance
print(values.var())

#third moment - skew
print(sp.skew(values))

#fourth momemt - kurtosis
print(sp.kurtosis(values))
