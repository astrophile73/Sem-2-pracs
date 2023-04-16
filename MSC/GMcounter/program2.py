import numpy as np
import matplotlib.pyplot as plt

## Avg counts
m1,m2= 5133.5,4194 ## m1, m2
m12,mb=9087.5,21 ## m12, mb

## Calculation of Time
T = (m1+m2-m12-mb)/(2*(m1-mb)*(m2-mb))
print(T)

# True count 
def true_count(T,m):
    n = m/(m*(1-(m*T)))
    return n

true1=true_count(T,m1)
true2=true_count(T,m2)
print(true1,true2)

