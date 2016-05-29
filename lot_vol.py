from euler import *
import matplotlib.pyplot as plt


def F1(y, t):
    """
    Modele de Malthus
    """
    return (births - deaths) * y


def F2(y, t):
    """
    Modele de Verhulst
    """
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
    plt.plot(x, eq1, 'r', label='Modele malthusien')
    plt.plot(x, eq2, 'b', label='Modele de Verhulst')
    plt.legend()
    plt.xlabel('Temps')
    plt.ylabel('Population')
    plt.title('Evolution d\'une population suivant deux modeles')
    plt.show()


def U(u, v):
    return u * (a - b * v)


def V(u, v):
    return v * (c * u - d)


def F_pp(y, t):
    return np.array([U(y[0], y[1]), V(y[0], y[1])])


def solve_eq2(y0, t0, N, h, equation):
    sol = euler2(y0, t0, N, h, equation)
    return sol


def periode(x, y, err=1):
    n = len(y)
    maxima = []
    for i in range(1, n-1):
        if y[i-1] <= y[i] and y[i+1] <= y[i]:
            maxima.append(i)
    count = len(maxima)
    if count <= 2:
        print('Pas assez de maximums, agrandissez l\'axe des ordonnees')
    else:
        periodique = True
        moyenne = 0
        per = 0
        for i in range(count):
            moyenne += y[maxima[i]]
            if moyenne > (i+1)*y[maxima[0]]+err or moyenne < (i+1)*y[maxima[0]]-err:
                print('La fonction n\'est pas periodique, impossible de calculer la periode')
                periodique = False
                break
        for i in range(count-1):
            per += x[maxima[i+1]]-x[maxima[i]]
            if per > (i+1)*(x[maxima[1]]-x[maxima[0]])+err or per < (i+1)*(x[maxima[1]]-x[maxima[0]])-err:
                print('La fonction n\'est pas periodique, impossible de calculer la periode')
                periodique = False
                break
        if periodique:
            print('la periode de la fonction est ' + str(per/float(count-1)))


def plot_proie_predat(y0, t0, N, h):
    x = [t0]
    sol = solve_eq2(y0, t0, N, h, F_pp)
    y1 = [sol[0][0]]
    y2 = [sol[0][1]]
    for i in range(N-1):
        x.append(x[i] + h)
        y1.append(sol[i+1][0])
        y2.append(sol[i+1][1])
    periode(x, y1, 100)
    periode(x, y2, 100)
    plt.plot(x, y1, 'r', label='Population proies')
    plt.plot(x, y2, 'b', label='Population predateurs')
    plt.legend()
    plt.xlabel('Temps')
    plt.ylabel('Populations')
    plt.title('Modele proie-predateur de Lotka-Volterra')
    plt.show()


def plot_proie_predat_couple(y0, t0, N, h):
    sol = solve_eq2(y0, t0, N, h, F_pp)
    y1 = [sol[0][0]]
    y2 = [sol[0][1]]
    for i in range(N-1):
        y1.append(sol[i+1][0])
        y2.append(sol[i+1][1])
    plt.plot(y1, y2)
    plt.xlabel('Population proies')
    plt.ylabel('Population predateurs')
    plt.title('Modele proie-predateur de Lotka-Volterra')
    plt.show()


def plot_solutions_proches(y0, t0, N, h, d, n):
    pas = d/float(2*n)
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            pop = y0 + np.array([pas*i, pas*j])
            sol = solve_eq2(pop, t0, N, h, F_pp)
            y1 = [sol[0][0]]
            y2 = [sol[0][1]]
            for k in range(N-1):
                y1.append(sol[k+1][0])
                y2.append(sol[k+1][1])
            plt.plot(y1, y2)
    plt.xlabel('Population proies')
    plt.ylabel('Population Predateurs')
    plt.title('Affichage des solutions autour de la condition initiale %s' % y0)
    plt.show()


############# Parametres #############


# taux de natalite
births = 3
# taux de mortalite
deaths = 1
# capacite d'accueil de l'environnement
kappa = 100


# population a l'instant t0
y0 = 10
t0 = 0
# N1 pour le modele malthusien qui overflow si trop d'iterations, N2 pour le systeme proie-predateur
N1 = 250
N2 = 50000
# N3 pour les solutions proches
N3 = 5300
h = 0.01


############# Systeme proies-predateurs #############


# populations initiales de proies et de predateurs
y01 = [100, 20]
# taux de reproduction des proies
a = 0.3
# taux de mortalite des proies
b = 0.03
# taux de reproduction des predateurs
c = 0.005
# taux de mortalite des predateurs
d = 0.1


plot_lotka_volterra(y0, t0, N1, h)
plot_proie_predat(y01, t0, N2, h)
plot_proie_predat_couple(y01, t0, N2, h)
plot_solutions_proches(y01, t0, N3, h, 5, 1)