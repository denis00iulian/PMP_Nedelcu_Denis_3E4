import pymc3 as pm
import numpy as np
import pandas as pd
import theano.tensor as tt
import seaborn as sns
import scipy.stats as stats
from scipy.special import expit as logistic
import matplotlib.pyplot as plt
import arviz as az

az.style.use('arviz-darkgrid')
z = np.linspace(-8, 8)
plt.plot(z, 1 / (1 + np.exp(-z)))
plt.xlabel('z')
plt.ylabel('logistic(z)')
if __name__ == 'main':
    admission = pd.read_csv("Admission.csv")
    y_1 = admission['Admission']
    x_n = ['GRE', 'GPA']
    x_1 = admission[x_n].values

    with pm.Model() as model_1:
        alpha = pm.Normal('alpha', mu=0, sd=10)
        beta = pm.Normal('beta', mu=0, sd=2, shape=len(x_n))
        miu = alpha + pm.math.dot(x_1, beta)
        theta = pm.Deterministic('theta', 1 / (1 + pm.math.exp(-miu)))
        bd = pm.Deterministic('bd', -alpha/beta[1] - beta[0]/beta[1] * x_1[:,0])
        yl = pm.Bernoulli('yl', p=theta, observed=y_1)
        idata_1 = pm.sample(2000, target_accept=0.9, return_inferencedata=True)

    idx = np.argsort(x_1[:,0])
    bd = idata_1.posterior['bd'].mean(("chain", "draw"))[idx]
    plt.scatter(x_1[:,0], x_1[:,1], c=[f'C{x}' for x in y_1])
    plt.plot(x_1[:,0][idx], bd, color='k')
    az.plot_hdi(x_1[:,0], idata_1.posterior['bd'], color='k')
    plt.xlabel(x_n[0])
    plt.ylabel(x_n[1])