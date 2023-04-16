import numpy as np
import math 
import matplotlib.pyplot as plt
NA,NB=5,5
N = NA+ NB
q = 320
omegaA, omegaB, qAv, omegaT = np.zeros(q+1),np.zeros(q+1),np.zeros(q+1),np.zeros(q+1)
for i in range(0,q):
    qA = i
    qAv[i]=qA
    omegaA[i]=(math.factorial(NA+qA-1))/(math.factorial(qA))*(math.factorial(NA-1))
    qB= q-qA
    omegaB[i]=(math.factorial(NB+qB-1))/(math.factorial(qB))*(math.factorial(NB-1))
    omegaT[i]=omegaA[i]*omegaB[i]

plt.scatter(qAv,omegaT)
xrange = (0,10)
plt.show()    
