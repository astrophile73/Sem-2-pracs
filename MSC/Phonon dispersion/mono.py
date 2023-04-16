import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## Global constants
m = 1
c = 1.5

def op(y,t,m,c):
    u1,z1,u2,z2,u3,z3 = y
    u1dot = z1
    z1dot = c*(u3+u2-2*u1)
    u2dot = z2
    z2dot = c*(u1+u3-2*u2)
    u3dot = z3
    z3dot = c*(u1+u2-2*u3)
    return u1dot,u2dot,u3dot,z1dot,z2dot,z3dot

tmax = 1
t = np.linspace(0,tmax,100)
y0= np.array([-15,0,5,0,(-5/3),0])
y1= np.array([15,0,-5,0,(5/3),0])
y2= np.array([0,5,0,5,0,5])
y3= np.array([0,15,0,5,0,(5/3)])
y = odeint(op,y0,t,args=(m,c))
y1 = odeint(op,y1,t,args=(m,c))
y2 = odeint(op,y2,t,args=(m,c))
y3 = odeint(op,y3,t,args=(m,c))
u1,u2,u3 = y[:,0],y[:,2],y[:,4]

# 1st plot
plt.plot(t,u1,label="1st atom")
plt.plot(t,u2,label="2n atom")
plt.plot(t,u3,label="3rd atom")
plt.legend()
plt.ylabel("Displacement from mean")
plt.show()

# for 2nd plot
# a=1
# k=np.linspace(-4/np.pi/a,4*np.pi/a,1000)
# omega = ((4*c)/m)**0.5*abs(np.sin(k*a)/2)
# plt.plot(k,omega)
# plt.axhline()
# plt.axvline()
# plt.show()