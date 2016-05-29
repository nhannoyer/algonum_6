from euler import euler2
from math import sqrt
import numpy as np

import matplotlib as plt
from math import sin


"""The function F represent the adaptation                                                                                                                                                                              
    enter: 
    return: """
def F(teta,t):
    g = 9.81
    l = 5
    m = 3
    return(np.array([teta[1],-g*m*sin(teta[0])/l]))


"""                                                                                                                                                                             
    enter:                                                                                                                                                                          
    return: """
def frequence_pendule(theta0,F):
    t0 = 0
    N = 20
    h = 0.25
    T1 = euler2(theta0,t0,N,h,F)
    return T1

t0 = 0
N = 20
h = 0.25
g = 9.81
l = 5
m = 3
theta01 = np.array([0.0,1.0])
theta02 = np.array([0.3,1.5])
t0 = 0
N=20
h=0.25
tf = t0 + 2*N*h
t = np.linspace(t0,tf,N)
y1 = frequence_pendule(theta01,F)
tmp=np.array([0.0]*len(y1))
for k in range(len(y1)):
        tmp[k]=y1[k][0]
y2 = frequence_pendule(theta02,F)
tmp2=np.array([0.0]*len(y2))
for k in range(len(y2)):
        tmp[k]=y2[k][0]

        
plt.plot(t,tmp,'b-')([theta01[1],-g*m*sin(theta01[0])/l])
plt.plot(t,tmp2,'g-')([theta02[1],-g*m*sin(theta02[0])/l]) 

plt.show()

    
