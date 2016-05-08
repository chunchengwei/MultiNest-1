# In this file, I compute the posterior from the ()_post_equal_weights.dat which has 3844 points
# The morphology of the resulting posterior is different and in the previous cases (posterior.py) and
# again the area withing the curve is not equal 1


import matplotlib.pyplot as plt
import numpy as np

def posterior(filename, npars, wp, nBIN):
    param=[]
    f=open(filename, 'r')
    for line in f:
        Data=line.split()
        try:
            param.append(float(Data[wp-1]))
        except IndexError:
            print Data        
    MAXparam=max(param); MINparam=min(param) 
# BINS is an array that contains the limits of the BINS in the histogram
    BINS=np.linspace(MINparam, MAXparam, nBIN)
    sizeBIN=BINS[1]-BINS[0]
# paramsBINS gives the medium point inside each bin
    paramsBINS=np.arange(MINparam+sizeBIN/2., MAXparam, sizeBIN)
    pointsBIN=[]
    for i in range(len(BINS)-1):        
        pointsBIN.append(0.)
        for j in range(len(param)):
           if param[j]>BINS[i] and param[j]<BINS[i+1]: 
               pointsBIN[i]+=1.
        pointsBIN[i]=pointsBIN[i]/len(param)
    plt.figure(4)
    plt.plot(paramsBINS, pointsBIN)
    plt.show()
    area=0
    for i in range(len(pointsBIN)):
        area+=sizeBIN*pointsBIN[i]
        #print area_post, postBIN[i], sizeBIN*postBIN[i]
    print area, sizeBIN, BINS[1]-BINS[0]

posterior('/Users/mariajosebenitocastano/Desktop/workspace/bayesian/CADENAS/chains7/prueba-post_equal_weights.dat', 3, 1, 50)
