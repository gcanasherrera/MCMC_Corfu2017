import matplotlib.pyplot as plt #Plot Libraries
import numpy as np #Maths arrays and more, matlab-type vectors/arrays
import sys #Strings inputs
import math #mathematical functions
from MCMC import MCMC

#Me creo objecto de la clase MCMC que coge los parametros del ___ini___
object_MCMC = MCMC(0, 1, 10000)
x_current = 1
object_MCMC.MCMC_exe(x_current)


possible_rho=[]
possible_lags=[]

for i in range (0, object_MCMC.N/2):
    possible_rho.append(object_MCMC.covariance_lag(i))
    possible_lags.append(i)

plt.figure()
plt.plot(possible_lags, possible_rho)
plt.show()
