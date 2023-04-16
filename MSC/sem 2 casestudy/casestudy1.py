import numpy as np
from scipy.integrate import odeint

def rk4(f,x0,y0,h):
    k1 = f(x0,y0)
    k2 = f(x0+h/2,y0/2*k1)
    k3 = f(x0+h/2,y0/2*k2)
    k4 = f(x0+h,y0+h*k3)

    yz = 1/6*(k1+2*k2+2*k3+k4)

    x1 = x0+h
    y1 = y0+h*yz

    return  x1,y1

def f(x,y): # y= un x = t
    y2 = (8000/4)()
    

