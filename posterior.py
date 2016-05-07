# This function takes as arguments the ().txt output file from a MultiNest 
# run and returns the marginalized posterior from the sample posterior

# npars is the dimension of the parameter space
# wp gives the parameter for which we construct the posterior distribution
# nBIN-1 is the number of bins in the posterior histogram
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

def posterior(filename, npars, wp, nBIN):
    sample_posterior=[]
    sample_logLike=[]
    param=[]
    f=open(filename, 'r')
    for line in f:
        Data=line.split()
        try:
            sample_posterior.append(float(Data[0]))
            sample_logLike.append(-0.5*float(Data[1]))
            param.append(float(Data[1+wp]))
        except IndexError:
            print Data        
    plt.figure(1)
    plt.scatter(param, sample_posterior)
    #plt.figure(2)
    #plt.scatter(parameter, sample_logLike)
    MAXparam=max(param); MINparam=min(param) 
# BINS is an array that contains the limits of the BINS in the histogram
    BINS=np.linspace(MINparam, MAXparam, nBIN)
    sizeBIN=BINS[1]-BINS[0]
# paramsBINS gives the medium point inside each bin
    paramsBINS=np.arange(MINparam+sizeBIN/2., MAXparam, sizeBIN)
# postBIN is the value of the posterior in each BIN
    #postBIN=[]
    pointsBIN=[]
    for i in range(len(BINS)-1):        
        #postBIN.append(0)
        pointsBIN.append(0.)
        for j in range(len(param)):
           if param[j]>BINS[i] and param[j]<BINS[i+1]: 
               #postBIN[i]+=sample_posterior[j]
               pointsBIN[i]+=1.
        #pointsBIN[i]=pointsBIN[i]/len(sample_posterior)
    #mean=0.682948; sd=0.12399
    #x=np.linspace(0., 1.5, 100)
    plt.figure(3)
    plt.plot(paramsBINS, pointsBIN)
    plt.hist(param, nBIN-1, color='white')
    #plt.plot(x, norm.pdf(x, mean, sd))
    #plt.figure(4)
    #plt.bar(BINS, pointsBIN)
    plt.show()
