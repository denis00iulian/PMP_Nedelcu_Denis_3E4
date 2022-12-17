import numpy as np
import arviz as az
import pymc3 as pm
import theano as tt

if __name__ == '__main__':
    clusters = 3
    n_cluster = [200, 150, 150]
    n_total = sum(n_cluster)
    mymeans = [5, 0, 5]
    std_devs = [2, 2, 2]
    mix = np.random.normal(np.repeat(mymeans, n_cluster), np.repeat(std_devs, n_cluster))
    az.plot_kde(np.array(mix))
    with pm.Model() as model_mgp:
        p = pm.Dirichlet('p', a=np.ones(clusters))
        means = pm.Normal('means', mu=np.array(mymeans) * mix.mean(), sd=2, shape=clusters)
        sd = pm.HalfNormal('sd', sd=2)
        order_means = pm.Potential('order_means', tt.switch(means[1]-means[0] < 0, -np.inf, 0))
        y = pm.NormalMixture('y', w=p, mu=means, sd=sd, observed=mix)
        idata_mgp = pm.sample(1000, random_seed=123, return_inferencedata=True)
    
    varnames = ['means', 'p']
    az.plot_trace(idata_mgp, varnames)