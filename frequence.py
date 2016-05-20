from euler import euler_n_step
from math import sqrt

def f(g,l,a1,a2):
    T = [0,0]
    T[0] = a2
    T[1] = -g/l*sin(a1)
    return T
    


def frequence_pendule(angle_initial,f,g,l):
    T1 = euler_n_step(angle_initial,0,20,1,f)
    return T1
    
print(T1)
