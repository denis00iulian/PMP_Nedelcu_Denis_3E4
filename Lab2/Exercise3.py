from scipy.stats import bernoulli
import matplotlib.pyplot as plt
p = 0.3
k = [0, 1]
pmf_X = bernoulli.pmf(k, p)


fig, ax = plt.subplots(1, 1)
ax.bar(k, pmf_X)
plt.ylabel("pmf")
plt.xlabel("k")
plt.title("Probability mass function")
plt.show()