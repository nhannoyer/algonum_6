from euler import *
import matplotlib.pyplot as plt


#taux de natalite 
births = 3  
#taux de mortalite
deaths = 1  
#capacite d'accueil de l'environnement
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
N = 2110
h = 0.01

#plot_lotka_volterra(y0, t0, N, h)


############# Systeme proies-predateurs #############


#populations initiales de proies et de predateurs
y01 = [100, 10]
#taux de reproduction des proies
a = 5
#taux de mortalite des proies
b = 1  
#taux de reproduction des predateurs
c = 0.5  
#taux de mortalite des predateurs
d = 5


def U(u, v):
    return u * (a - b * v)


def V(u, v):
    return v * (c * u - d)


def F_pp(y, t):
    return np.array([U(y[0], y[1]), V(y[0], y[1])])


def solve_eq2(y0, t0, N, h, equation):
    sol = euler2(y0, t0, N, h, equation)
    return sol


def plot_proie_predat(y0, t0, N, h):
    x = [t0]
    sol = solve_eq2(y0, t0, N, h, F_pp)
    y1 = [sol[0][0]]
    y2 = [sol[0][1]]
    for i in range(N-1):
        x.append(x[i] + h)
        y1.append(sol[i+1][0])
        y2.append(sol[i+1][1])
    plt.plot(x, y1, 'r', x, y2, 'b')
    plt.show()


#plot_proie_predat(y01, t0, N, h)


def plot_proie_predat2(y0, t0, N, h):
    sol = solve_eq2(y0, t0, N, h, F_pp)
    y1 = [sol[0][0]]
    y2 = [sol[0][1]]
    for i in range(N-1):
        y1.append(sol[i+1][0])
        y2.append(sol[i+1][1])
    plt.plot(y1, y2)
    plt.show()

plot_proie_predat2(y01, t0, N, h)
