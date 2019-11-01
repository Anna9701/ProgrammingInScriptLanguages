import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def my_fun(x):
    return (np.sin(3 * x) ** 2) / x

def ir1(xw, yw, i): #Iloraz roznicowy pierwszego stopnia
    return (yw[i+1] - yw[i]) / (xw[i+1] - xw[i])

def ir2(xw, yw, i): #Iloraz roznicowy drugiego stopnia
    return (ir1(xw, yw, i+1) - ir1(xw, yw, i)) / (xw[i+2] - xw[i])

def ir3(xw, yw, i): #Iloraz roznicowy trzeciego stopnia
    return (ir2(xw, yw, i+1) - ir2(xw, yw, i)) / (xw[i+3] - xw[i])

def i_r(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)

def newton(xw, yw):
    tab = [yw[:]]
    n = len(yw)
    for k in range(n-1):
        j = n - 1 - k
        tmp = []
        for m in range(j):
            tmp.append(i_r(tab[k][m], tab[k][m + 1], xw[m], xw[m + k + 1]))
        tab.append(tmp)
    return [t[0] for t in tab]

def W(tab, wx, x):
    sum = 0
    for i in range(len(wx)):
        product = 1
        for j in range(i):
            product *= x - wx[j]
        sum += product * tab[i]
    return sum


def my_inertpld(xw, yw):
    def f(x):
        j = 0
        for i in range(0, len(xw) - 1):
            if xw[i] <= x <= xw[i + 1]:
                break
            j += 1
        return (x-xw[j]) * (yw[j+1] - yw[j-1]) / (xw[j+1] - xw[j]) + yw[j]
    return f

a = 1
b = 3
xp = np.linspace(a, b)
fp = my_fun(xp)

x_nodes = np.linspace(a, b, 5)
y_nodes = my_fun(x_nodes)

y_numpy_interp = np.interp(xp, x_nodes, y_nodes)

f_scipy_interp = interp1d(x_nodes, y_nodes, kind='cubic')
y_scipy_interp = f_scipy_interp(xp)

y_i1 = [my_inertpld(x_nodes, y_nodes)]

x_w = np.array([1., 1.5, 2., 2.5, 3.])
y_w = my_fun(x_w)

n = newton(x_w, y_w)

y_i2 = [W(n, x_w, i) for i in xp]

plt.plot(xp, fp, "g-", xp, y_scipy_interp, "b.-", xp, y_numpy_interp, "r.:", xp, y_i2, "k.-")
plt.legend(['function', 'scipy_interpld', 'numpy_interp', 'newton'], loc='best')
plt.show()