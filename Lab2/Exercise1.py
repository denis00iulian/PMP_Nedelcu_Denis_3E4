import numpy as np
import matplotlib.pyplot as plt
import random

def chooseMechanic():
    randValue = random.random()
    if randValue < 0.4:
        return 'first'
    else:
        return 'second'

np.random.seed(1)

firstMechanicAlpha = 4
secondMechanicAlpha = 6
n = 10000
r_values = list(range(n))
X = []
for i in range(n):
    if chooseMechanic() == 'first':
        X.append(np.random.exponential(scale=1/firstMechanicAlpha))
    else:
        X.append(np.random.exponential(scale=1/secondMechanicAlpha))

print("Mean =", np.mean(X), "\nStd =", np.std(X))
fig, ax = plt.subplots(1, 1)
ax.bar(r_values, X)
plt.show() 
