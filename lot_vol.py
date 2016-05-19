from euler import *
import matplotlib.pyplot as plt


births = 3
deaths = 1
kappa = 100


def F1(y, t):
    return (births - deaths) * y


def F2(y, t):
    return (births - deaths) * y * (1 - y/kappa)


def solve_eq(y0, t0, N, h, equation):
    sol = euler_n_step(y0, t0, N, h, equation)
    return sol


def plot_lotka_volterra(y0, t0, N, h):
    x = [t0]
    for i in range(N-1):
        x.append(x[i] + h)
    eq1 = solve_eq(y0, t0, N, h, F1)
    eq2 = solve_eq(y0, t0, N, h, F2)
    plt.plot(x, eq1, 'r', x, eq2, 'b')
    plt.show()


y0 = 10  #population a l'instant t0
t0 = 0
N = 100
h = 0.01

plot_lotka_volterra(y0, t0, N, h)

#a = 
#b = 
#c = 
#d = 

#def proie_predat(y0, t0, N, h):
#    x = [t0]
#    for i in range(N-1):
#        x.append(x[i]+h)
        
