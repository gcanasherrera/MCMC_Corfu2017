import matplotlib.pyplot as plt #Plot Libraries
import numpy as np #Maths arrays and more, matlab-type vectors/arrays
import sys #Strings inputs
import math #mathematical functions
from MCMC import MCMC

#Me creo objecto de la clase MCMC que coge los parametros del ___ini___
object_MCMC = MCMC(0, 1, 10000)
x_current = 1
object_MCMC.MCMC_exe(x_current)
