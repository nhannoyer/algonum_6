from euler import euler2
from math import sqrt
import numpy as np

import matplotlib.pyplot as plt
from math import sin


"""The function F represent the transformation
    to adapt a second degree differencial equation                                                                                                                                                                            
    enter: theta the variable represented the variations of angle
           t     the variable represented the variations of time
    return: The fonction F as describe above """

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


plt.plot(t,y1)
plt.plot(t,y2)
plt.legend()
plt.xlabel('Temps')
plt.ylabel('frequence')
plt.title('Evolution de la frequence du pendule dans le temps')
plt.show()

plt.plot(t,tmp,'b')
plt.plot(t,tmp2,'r')
plt.show()


#####    Affichage des differentes positions prises en fonction    #####
#####      des valeurs initiales pour un pendule a 1 maillon       #####


# Methode d Euler adaptee au pendule

def step_euler2(y,t,h,f):
    return np.array(y + h*f(y,t))
                
def euler2(y0,t0,N,h,f):
    y = np.array([[0.0,0.0]]*N)
    y[0] = y0
    T = np.array([(t0 + 6*h*i) for i in range(N)])
    for k in range (N-1):
        y[k+1] = step_euler2(y[k],T[k],h,f)
    return np.array(y)


# Fonction permettant l utilisation d'une equadif
# d'ordre 2 en equadif d ordre 1 (grace a un vecteur)

def F2(teta,t):
    g = 9.81
    l = 5
    return(np.array([teta[1],-g*m*sin(teta[0])/l]))
    

# Valeurs initiales:
    
# Petites valeurs

y5 = np.array([0.0,0.1]) 
y6 = np.array([0.0,0.2])
y7 = np.array([0.0,0.4])
y8 = np.array([0.0,0.6])
y9 = np.array([0.0,0.8])

# Valeur plus elevee

y10 = np.array([0.0,2.0])


# Initialisation des parametres et du temps

t0 = 0.0
y0 = 1.0
N = 20
h = 0.25
tf = t0 + N*h
t = np.linspace(t0,tf,N)


# Fonction permettant d obtenir le tableau des positions du 
# pendule en fonction du temps

def frequence(y0,t0,N,h,F):
    y = euler2(y0,t0,N,h,F)
    tmp=np.array([0.0]*len(y))
    for k in range(len(y)):
        tmp[k]=y[k][0]
    return tmp
    
    
# Creation des tableaux pour les differentes valeurs initiales

f1 = frequence(y5,t0,N,h,F2)
f2 = frequence(y6,t0,N,h,F2)
f3 = frequence(y7,t0,N,h,F2)
f4 = frequence(y8,t0,N,h,F2)
f5 = frequence(y9,t0,N,h,F2)
f6 = frequence(y10,t0,N,h,F2)


# Affichage des courbes correspondantes
        
plt.plot(t,f1)
plt.plot(t,f2)
plt.plot(t,f3)
plt.plot(t,f4)
plt.plot(t,f5)
plt.plot(t,f6)
 
plt.show()

