# Orders the parameters form minimum to maximum value and de sample posterior equivalently
# I know how to get the mean value for a parameter. Now I want to understand what this value means:
# (A) Does it mean that the area within the marginal or joint p.d.f up this mean value equals 0.5?

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

order_param=[]  # Contains the paramaters ordered where order_param[0] equals the minimum value and
                # order_params[7599] equals the maximum value
order_post=[]   # the corresponded sample posterior weight

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

mean=0
for i in range(len(order_param)):
    mean+=order_param[i]*order_post[i]

# Computing the area within the marginal or joint? (I do not know which one I am computing with this method)
# up to the mean value:

area_down=0
for i in range(len(sample_post)):
    area_down+=sample_post[i]
    if area_down > 0.5 :
        print area_down, order_param[i], i
        break
