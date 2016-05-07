# Computation of mean, standard deviations and covariance of the parameters from the posterior sample

f=open('/Users/mariajosebenitocastano/Desktop/workspace/bayesian/CADENAS/chains7/prueba-.txt', 'r')
post=[]; alpha=[]; rs=[]; rho=[]
for line in f:
    Data=line.split()
    try:
        post.append(float(Data[0]))
        alpha.append(float(Data[2]))
        rs.append(float(Data[3]))
        rho.append(float(Data[4]))
    except IndexError:
        print Data

product_alpha=[]; product_rs=[]; product_rho=[]
#alpha2=[]; product_alpha2=[]; 
product_alpha_rs=[]
product_alpha_rho=[]; product_rs_rho=[]
for i in range(len(alpha)):
    product_alpha.append(alpha[i]*post[i])
    #alpha2.append(alpha[i]**2)
    product_alpha_rs.append(alpha[i]*rs[i]*post[i])
    product_alpha_rho.append(alpha[i]*rho[i]*post[i])
    product_rs_rho.append(rs[i]*rho[i]*post[i])
    #product_alpha2.append(alpha[i]**2*post[i])
    product_rs.append(rs[i]*post[i])
    product_rho.append(rho[i]*post[i])
mean_alpha=sum(product_alpha)
#mean_alpha2=sum(product_alpha2)
mean_rs=sum(product_rs)
mean_rho=sum(product_rho)

cov_alpha_rs=sum(product_alpha_rs)-mean_alpha*mean_rs
cov_alpha_rho=sum(product_alpha_rho)-mean_rho*mean_alpha
cov_rs_rho=sum(product_rs_rho)-mean_rs*mean_rho
