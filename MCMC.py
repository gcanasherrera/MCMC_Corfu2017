# Name: MCMC.py
#
# Corfu 2017
#
# Type: python class
#
# Content: 1 Class, 1 constructor, 5 methods
#
# Description: General Class destinated to get a cross-matching process between two catalogs from different filtered images


__author__ = ""
__copyright__ = "Copyright (C) 2017 G. Canas Herrera"
__license__ = "Public Domain GNU"
__version__ = "1.0.0"
__maintainer__ = "Guadalupe Canas Herrera"
__email__ = "canasherrera@lorentz.leidenuniv.nl"


import matplotlib.pyplot as plt #Plot Libraries
import numpy as np #Maths arrays and more, matlab-type vectors/arrays
import sys #Strings inputs
import math #mathematical functions
#import subprocess #calling to the terminal
#from astropy.io import fits #Open and Reading FITS Files usign astropy
import random #pseudo-random generator
#import seaborn as sns #Improvements for statistical-plots
#from pymodelfit import FunctionModel1DAuto #Create own model of fitting
from scipy import spatial #KDTREE altorithm
import seaborn as sns


"""
    General Class that contents several methods destinated to get a cross-matching between two catalogs
    
    """
class MCMC(object):
    
    
    """
        Constructor that defines attribute of future class-objects
    """
    
    def __init__(self, gaussian_mean, gaussian_std, chain_length):  #define attributes of future class-objects
        # catalog_2 and catalog_2 are objects from Class_CatalogReader.py
        self.gaussian_mean = 0.
        self.gaussian_std = 1.
        self.chain=[]
        self.function=[]
        self.N=chain_length

#    def jump_gaussian(x):
#        return 1./(self.gaussian_std*(np.sqrt(2*np.pi))) * np.exp(-0.5*((x-self.gaussian_mean)/self.gaussian_std)**2)

    def target_distribution(self, x):
        if x < 0:
            return  0
        else:
            return np.exp(-x)


    def x_prop(self, x):
        generate_random= np.random.normal(self.gaussian_mean, self.gaussian_std)
        return x + generate_random


    def MCMC_exe(self, x_current):
        
        
        for i in range (0, self.N):
            #print i
            x_prop = self.x_prop(x_current)
            
            A = self.target_distribution(x_prop)/self.target_distribution(x_current)
            
            generator =np.random.uniform(0, 1, 1)
            
            
            if A >= 1:
                x_current = x_prop
            else:
                if generator < A:
                    x_current = x_prop
            
            print x_current

            self.chain.append(x_current)
            self.function.append(self.target_distribution(x_current))

        #plt.hist(self.chain, bins='auto')
        #plt.plot(self.chain, self.function, '-')
        sns.distplot(self.chain, color="m")
        #plt.tight_layout()
        plt.show()







































