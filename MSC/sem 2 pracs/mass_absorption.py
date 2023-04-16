import numpy as np 
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

Althickness=np.array([.05,.1,.15,.2,.25,.3,.35,.4,.45],dtype='float64')
counts=[3944,2918,2244,1895,1456,1273,701,511,515]
def mapping(Althickness,I0,a):
    return (I0*(np.exp(-a*Althickness)))
args,covar=curve_fit(mapping,Althickness,counts)
print("Arguments:",args)
I0,a=args[0],args[1]
e=np.exp(-a*Althickness)
y_fit=I0*e


rho = 2710 #kg/m^3
Abscoeff=a/rho
print(Abscoeff)


plt.plot(Althickness,counts,label="Original")
plt.plot(Althickness,y_fit,label="Fitted curve")

plt.legend()
plt.show()