import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import arviz as az

np.random.seed(1)

firstMechanicAlpha = 4
firstMechanicTime = stats.expon.rvs(scale = 1 / firstMechanicAlpha, size = 10000)
secondMechanicAlpha = 6
secondMechanicTime = stats.expon.rvs(scale = 1 / secondMechanicAlpha, size = 10000)
            


az.plot_posterior({'x':firstMechanicTime,'y':secondMechanicTime}) # Afisarea aproximarii densitatii probabilitatilor, mediei, intervalului etc. variabilelor x,y,z
plt.show() 
