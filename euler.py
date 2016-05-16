import math as m
import numpy as np
import matplotlib.pyplot as plt

def step_euler(y,t,h,f):
   	return(y + h*f(y,t))

def euler_n_step(y0,t0,N,h,f):
    y = np.array([0.0]*N)
    y[0] = y0
    T = np.array([(t0 + h*i) for i in range(N)])
    for k in range (N-1):
        y[k+1] = step_euler(y[k],T[k],h,f)
    return np.array(y)


 
def F(y,t):
    return y


t0 = 0.0
y0 = 1.0
N = 100
h = 0.01
tf = t0 + N*h

t = np.linspace(t0,tf,N)
y = euler_n_step(y0,t0,N,h,F)
plt.plot(t,y,'b-')
plt.plot(t,np.exp(t),'r--')
plt.show()
