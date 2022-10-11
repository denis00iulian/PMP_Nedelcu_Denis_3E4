from scipy import stats
import matplotlib.pyplot as plt
import arviz as az

latency = stats.expon.rvs(scale=1/4, size=1000)
firstServer = stats.gamma.rvs(4, scale=1/3, size=1000) + latency
secondServer = stats.gamma.rvs(4, scale=1/2, size=1000) + latency
thirdServer = stats.gamma.rvs(5, scale=1/2, size=1000) + latency
forthServer = stats.gamma.rvs(5, scale=1/3, size=1000) + latency
P_First = 0.25
P_Second = 0.25
P_Third = 0.3
P_Forth = 0.2

az.plot_posterior({'1st':firstServer, '2nd':secondServer, '3rd':thirdServer, '4th':forthServer})
plt.show()