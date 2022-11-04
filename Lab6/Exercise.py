import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import arviz as az


if __name__ == '__main__':
    file = open("E:\FACULTATE\Anul 3\Sem 1\PMP\PMP_Nedelcu_Denis_3E4\Lab6\data.csv")

    data = pd.read_csv(file)

    ppvtMean = data['ppvt'].mean()
    ppvtStddev = data['ppvt'].std()
    momAgeMean = data['momage'].mean()
    momAgeStddev = data['momage'].std()

    alpha_real = momAgeMean
    beta_real = momAgeStddev
    eps_real = np.random.normal(0, 0.5, size=100)

    x = np.random.normal(momAgeMean, momAgeStddev, 100)
    y_real = alpha_real + beta_real * x
    y = y_real + eps_real
    with pm.Model() as model_g:
        alpha = pm.Normal('alpha', mu=momAgeMean, sd=momAgeStddev)
        beta = pm.Normal('beta', mu=ppvtMean, sd=ppvtStddev)
        eps = pm.HalfCauchy('eps', 5)
        mu = pm.Deterministic('mu', alpha + beta * x)
        y_pred = pm.Normal('y_pred', mu=mu, sd=eps, observed=y)
        idata_g = pm.sample(2000, tune=2000, return_inferencedata=True)

    az.plot_trace(idata_g, var_names=["alpha", "beta", "eps"])

# fig, ax = plt.subplots(1, 1)
# ax.bar(momAgeValues, ppvtAverage)
# plt.show()

    file.close()