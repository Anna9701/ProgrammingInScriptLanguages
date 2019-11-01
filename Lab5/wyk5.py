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

x_w = np.array([-1., 0., 1., 2.])
y_w = np.array([-4., -1., 0., 5.])
ir_11 = ir1(x_w, y_w, 0)
ir_12 = ir1(x_w, y_w, 1)
ir_13 = ir1(x_w, y_w, 2)

ir_21 = ir2(x_w, y_w, 0)
ir_22 = ir2(x_w, y_w, 1)

ir_31 = ir3(x_w, y_w, 0)

# def ir_k(xw, yw, i, k = 0):
#     k += 1
#     x = []
#     if k + i < len(xw):
#         x.append((ir_k(xw, yw, i + k) - ir_k(xw, yw, i + k - 1)) / (xw[i + k] - xw[i]))
#     return x

def i_r(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)

def newton(xw, yw):
    tab = [yw[:]]
    n = len(yw)
    for k in range(n-1):
        j = n - 1 - k
        tmp = []
        for m in range(j):
            tmp.append(i_r(tab[k][m], tab[k][m+1], xw[m], xw[m+1]))
        tab.append(tmp)
    return [t[0] for t in tab]

n = newton(x_w, y_w)

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

xp = np.linspace(1, 3)
fp = my_fun(xp)

y_i2 = [W(n, x_w, i) for i in xp]

x_nodes = np.linspace(1, 3, 5)
y_nodes = my_fun(x_nodes)

#f_in = interp1d(x_nodes, y_nodes, kind='cubic')
#y_in = f_in(xp)

y_i1 = [my_inertpld(x_nodes, y_nodes)]

plt.plot(xp, fp, "g-", x_nodes, y_nodes, "ro", xp, y_i2)
plt.legend(['function', 'nodes', 'i2'], loc='best')
plt.show()