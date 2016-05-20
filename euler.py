import math as m
import numpy as np
import matplotlib.pyplot as plt


##################### Methode d'Euler #####################

def step_euler(y,t,h,f):
   	return(y + h*f(y,t))

def euler_n_step(y0,t0,N,h,f):
    y = np.array([0.0]*N)
    y[0] = y0
    T = np.array([(t0 + h*i) for i in range(N)])
    for k in range (N-1):
        y[k+1] = step_euler(y[k],T[k],h,f)
    return np.array(y)


##################### Methode du point milieu #####################

def step_pt_milieu(y,t,h,f):
	a = f(y,t)
	b = f(y + a*h/2,t + h/2)
	return(y + h*b)

def pt_milieu_n_step(y0,t0,N,h,f):
	y = np.array([0.0]*N)
	y[0] = y0
	T = np.array([(t0 + h*i) for i in range(N)])
	for k in range (N-1):
		y[k+1] = step_pt_milieu(y[k],T[k],h,f)
	return np.array(y)


##################### Methode de Heun #####################

def step_heun(y,t,h,f):
	a = f(y,t)
	b = f(y + a*h*2/3,t + h*2/3)
	return(y + (h/4)*(a + 3*b))

def heun_n_step(y0,t0,N,h,f):
	y = np.array([0.0]*N)
	y[0] = y0
	T = np.array([(t0 + h*i) for i in range(N)])
	for k in range (N-1):
		y[k+1] = step_heun(y[k],T[k],h,f)
	return np.array(y)


##################### Methode de Runge-Kutta #####################

def step_rungek(y,t,h,f):
	a = f(y,t)
	b = f(y + a*h/2,t + h/2)
	c = f(y + b*h/2,t + h/2)
	d = f(y + c*h,t + h)
	return(y + (a + 2*b + 2*c + d)*h/6)

def rungek_n_step(y0,t0,N,h,f):
	y = np.array([0.0]*N)
	y[0] = y0
	T = np.array([(t0 + h*i) for i in range(N)])
	for k in range (N-1):
		y[k+1] = step_rungek(y[k],T[k],h,f)
	return np.array(y)

##################### Fonction generiques #####################

def meth_n_step(y0,t0,N,h,f,meth):
        meth = "step_" + meth
        y = np.array([0.0]*N)
        y[0] = y0
        T = np.array([(t0 + h*i) for i in range(N)])
        for k in range (N-1):
                y[k+1] = step_(y[k],T[k],h,f)
        return np.array(y)

#def meth_epsilon(y0,t0,tf,eps,f,meth):
#        y = np.array([0.0]*)



#################### Pendule a 1 maillons

def step_euler2(y,t,h,f):
   	return np.array(y + h*f(y,t))

def euler2(y0,t0,N,h,f):
    y = np.array([0.0,0.0]*N)
    y[0] = y0
    T = np.array([(t0 + h*i) for i in range(N)])
    for k in range (N-1):
        y[k+1] = step_euler2(y[k],T[k],h,f)
    return np.array(y)

def F2(teta,t):
        g = 9.81
        l = 5
        return(np.array([teta[1],-g*m.sin(teta[0])/l]))

y2 = np.array[0.0,0.0]
t2 = 0.0

##################### Tests #####################

def F(y,t):
    return y

t0 = 0.0
y0 = 1.0
N = 20
h = 0.25
tf = t0 + N*h

t = np.linspace(t0,tf,N)
y1 = euler_n_step(y0,t0,N,h,F)
y2 = pt_milieu_n_step(y0,t0,N,h,F)
y3 = heun_n_step(y0,t0,N,h,F)
y4 = rungek_n_step(y0,t0,N,h,F)

y = euler2(y2,t2,N,h,F2)
plt.plot(t,y[0],'b-')

#plt.plot(t,y1,'b-')
#plt.plot(t,y2,'g-')
#plt.plot(t,y3,'b-')
#plt.plot(t,y4,'b-')

#plt.plot(t,np.exp(t),'r--')
plt.show()




