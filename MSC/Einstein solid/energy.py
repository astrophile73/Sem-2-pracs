import numpy as np
import math 
import matplotlib.pyplot as plt
NA,NB=100,500
qA,qB=300,0
q = qA+qB
N= NA+NB
state = np.zeros(N,float)
pa = np.random.randint(0,NA,(qA,1))
for ip in range(len(pa)):
    i=pa[ip]
    state[i]=state[i]+1
    
pb = np.random.randint(0,NB,(qB,1))
for ip in range(len(pb)):
    i=pb[ip]
    state[i]=state[i]+1 

plt.ylim(0,30)   
plt.xlim(0,100)
plt.plot((np.arange(0,N)),state,'r')
plt.xlabel('i')
plt.ylabel('n_i')
plt.show()

ns = 1000
EA,EB =np.zeros(ns,float),np.zeros(ns,float)
for i in range(ns):
    i1 = np.random.randint(0,N)
    if(state[i]>0):
        i2= np.random.randint(0,N)
        state[i2]=state[i2]+1
        state[i1]=state[i1]-1
EA[i]= sum(state[0:NA-1])
EB[i]=q-EA[i]
