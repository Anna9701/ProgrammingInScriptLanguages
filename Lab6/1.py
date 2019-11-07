import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 4, 100)
y1 = x ** 3 + 2 * x ** 2 + 10
y2 = 3 * x ** 2 + 4 * x

fig, ax = plt.subplots()
ax.plot(x, y1, color = "blue", label = "y(x)")
ax.plot(x, y2, color = "red", label = "y'(x)")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()
