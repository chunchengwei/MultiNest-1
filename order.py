# Orders the parameters form minimum to maximum value and de sample posterior equivalently

import numpy as np
sample_posterior=[]
param1=[]
param2=[]
f=open('/Users/mariajosebenitocastano/Desktop/workspace/bayesian/CADENAS/chains7/prueba-.txt', 'r')
for line in f:
    Data=line.split()
    try:
       sample_posterior.append(float(Data[0]))
       param1.append(float(Data[2]))
 
    except IndexError:
        print Data
product_param1=[]; 
for i in range(len(param1)):
    product_param1.append(param1[i]*sample_posterior[i])

mean_param1=sum(product_param1)

order_param=[]
order_post=[]

while param1:
    minimum=param1[0]
    j=0
    for i in range(len(param1)):
        x=param1[i]
        if x<minimum:
            minimum=x
            j=i
    order_param.append(minimum)
    order_post.append(sample_posterior[j])
    param1.remove(minimum)
    sample_posterior.remove(sample_posterior[j])
