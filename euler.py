import math as m
import numpy as np

def step_euler(y,t,h,f):
    y[t+h] = y[t] + h*F(y[t],t)
    return y

def euler_n_step(y0,t0,N,h,f):
    y = [0]*N
    y[0] = y0
    t = [(t0 + h*i) for i in range(N)]
    for k in range (N):
        step_euler(y,t[i],h,f)
    return y


def euler(F,y0,t):
    N = len(t)
    y = [0]*N
    y[0] = y0
    for i in range(N-1):
        y[i+1] = y[i]+(t[i+1]-t[i])*F(y[i],t[i])
    return y
 
