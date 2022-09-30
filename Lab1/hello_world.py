import matplotlib.pyplot as plt

import numpy as np

import pymc3 as pm

# Generating data
# True parameter values
alpha, sigma, mu = 1, 1, 0
sigma2 = 2
beta = [1, 2.5]

# Size of dataset
size = 100

# Predictor variable
X1 = np.random.randn(size)
X2 = np.random.randn(size) * 0.2
X3 = np.random.normal(mu, sigma2, size)

# Simulate outcome variable
Y = alpha + beta[0] * X1 + beta[1] * X2 + np.random.randn(size) * sigma
Y2 = 1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (X3 - mu)**2 / (2 * sigma2**2) )

# Vizualize the data
fig, axes = plt.subplots(1, 3, sharex=True, figsize=(10, 4))
axes[0].scatter(X1, Y, alpha=0.6)
axes[1].scatter(X2, Y, alpha=0.6)
axes[2].scatter(X3, Y2, alpha=0.6)
axes[0].set_ylabel("Y")
axes[0].set_xlabel("X1")
axes[1].set_xlabel("X2")
axes[2].set_xlabel("X3")
plt.show()

# Define a model
basic_model = pm.Model()

with basic_model:

    # Priors for unknown model parameters
    alpha = pm.Normal("alpha", mu=0, sigma=10)
    beta = pm.Normal("beta", mu=0, sigma=10, shape=2)
    sigma = pm.HalfNormal("sigma", sigma=1)

    # Expected value of outcome
    mu = alpha + beta[0] * X1 + beta[1] * X2

    # Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=Y)

#Fit model to data and print estimates
map_estimate = pm.find_MAP(model=basic_model)
print(map_estimate)