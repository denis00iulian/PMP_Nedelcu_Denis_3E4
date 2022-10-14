import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc3 as pm
import arviz as az


if __name__ == '__main__':
    model = pm.Model()

    with model:
        cutremur = pm.Bernoulli('C', 0.005)
        incendiu = pm.Deterministic('I', pm.math.switch(cutremur, 0.03, 0.01))
        P_declansareAlarma = pm.Deterministic('DA_p', pm.math.switch(incendiu, pm.math.switch(cutremur, 0.98, 0.95), pm.math.switch(cutremur, 0.02, 0.001)))
        declansareAlarma = pm.Bernoulli('DA', p=P_declansareAlarma, observed=0)
        trace = pm.sample(20000)
        
    dictionary = {
                'cutremur': trace['C'].tolist(),
                'incendiu': trace['I'].tolist()
                }
    df = pd.DataFrame(dictionary)

    p_incendiu = df[(df['incendiu'] == 1)].shape[0] / df.shape[0]
    print(p_incendiu)