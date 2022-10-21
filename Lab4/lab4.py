import pymc3 as pm
import pandas as pd


if __name__ == '__main__':
    model = pm.Model()
    mean = 1
    alpha = 1/mean

    with model:
        nrClienti = pm.Poisson('C', mu=20) #clienti/ora
        tPlasareComanda = pm.Normal('Plasare', mu=1, sigma=0.5) #timp plasare comanda in minute
        tPregatireComanda = pm.Exponential("Pregatire", lam=alpha)
        trace = pm.sample(10000)

    dictionary = {
                    'nrClienti': trace['C'].tolist(),
                    'tPlasare': trace['Plasare'].tolist(),
                    'tPregatire': trace['Pregatire'].tolist()
                    }
    df = pd.DataFrame(dictionary)

    p_servire = df[((df['tPlasare'] + df['tPregatire']) * df['nrClienti'] < 15)].shape[0] / df.shape[0] #probabilitatea de a servi toti clientii care intra intr-o ora in mai putin de 15 minute
    print(p_servire * 100) #probabilitatea exprimata in %