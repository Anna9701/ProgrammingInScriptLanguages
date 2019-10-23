import numpy as np
import matplotlib.pyplot as plt

def chart_test():
    x = np.arange(1, 6)
    y = np.sin(x) * 5 + 3
    plt.plot(x, y, "o", color = "salmon")
    plt.plot(x, y - 2, "-", color = "blue")
    plt.show()

def t1():
    a = np.array([[-2, 1, 6],
                 [1, -2, -1],
                  [4, 1, 2]])
    b = np.array([5, -7.5, 9])
    x = np.linalg.solve(a, b)
    print(x)
    print(np.allclose(np.dot(a, x), b))

def t2():
    A = np.arange(1, 101).reshape(10, 10).transpose()
    B = np.arange(100, 0, -1).reshape(10, 10)
    C = A + B
    print(C)
    C[1, -1] = 2 * C[1, -1]
    print(C)
    print("Median: " + str(np.median(C)))
    x = np.ptp(C, axis = 0) # max - min
    y = np.ptp(C, axis = 1) # max - min
    print(x)
    print(y)

print("a: ")
a = float(input())
print("b: ")
b = float(input())
print("c: ")
c = float(input())

p = np.poly1d([a, b, c])
if len(p.r) == 2:
    if p.r[0] < p.r[1]:
        range = (p.r[1] - p.r[0]) * 3
    else:
        range = (p.r[0] - p.r[1]) * 3
    x = np.arange(0 - range, 0 + range, 0.1)
    y = p(x)
    plt.plot(x, y, "+", color = "red")
    plt.show()