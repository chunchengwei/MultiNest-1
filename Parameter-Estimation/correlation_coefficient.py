# The function "correlation_coefficient" computes the estimated correlation
# coefficient for parameters wp1 and wp2

def correlation_coefficient(filename, npar, wp1, wp2):
    import numpy as np
    sample_posterior=[]
    param1=[]
    param2=[]
    f=open(filename, 'r')
    for line in f:
        Data=line.split()
        try:
           sample_posterior.append(float(Data[0]))
           param1.append(float(Data[1+wp1]))
           param2.append(float(Data[1+wp2])) 
        except IndexError:
            print Data
    product_param1=[]; product_param2=[]; 
    product_param1_square=[]; product_param2_square=[]
    product_param1_param2=[]
    for i in range(len(param1)):
        product_param1.append(param1[i]*sample_posterior[i])
        product_param2.append(param2[i]*sample_posterior[i])
        product_param1_param2.append(param1[i]*param2[i]*sample_posterior[i])
        product_param1_square.append(param1[i]**2*sample_posterior[i])
        product_param2_square.append(param2[i]**2*sample_posterior[i])
    mean_param1=sum(product_param1)
    mean_param2=sum(product_param2)
    mean_param1_square=sum(product_param1_square)
    mean_param2_square=sum(product_param2_square)
    mean_param1param2=sum(product_param1_param2)
    
    r=(mean_param1param2-mean_param1*mean_param2)/ \
       np.sqrt((mean_param1_square-mean_param1**2)*(mean_param2_square-mean_param2**2))
    print r
    return r
    
correlation_coefficient('/Users/mariajosebenitocastano/Desktop/workspace/bayesian/CADENAS/chains7/prueba-.txt', 3, 1, 2)
correlation_coefficient('/Users/mariajosebenitocastano/Desktop/workspace/bayesian/CADENAS/chains7/prueba-.txt', 3, 1, 3)
correlation_coefficient('/Users/mariajosebenitocastano/Desktop/workspace/bayesian/CADENAS/chains7/prueba-.txt', 3, 2, 3)
