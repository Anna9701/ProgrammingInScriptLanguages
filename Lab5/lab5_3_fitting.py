import numpy as np
import matplotlib.pyplot as plt

N = 50

theta = np.linspace(0, 2 * np.pi, N)
r = 10

x1 = r * np.cos(theta)
x2 = r * np.sin(theta)
x1_noised = x1 + np.random.rand(N) - 0.5
x2_noised = x2 - np.random.rand(N) + 0.5

B = np.array([x1_noised, x2_noised]).transpose()
B = np.c_[B, np.ones(N)]
rank_B = np.linalg.matrix_rank(B)
col_B = B.shape[1]

b = np.zeros((N, 1))
for i in range(N):
    b[i, 0] = - (x1_noised[i] ** 2 + x2_noised[i] ** 2)

A = - np.copy(b)
A = np.c_[A, x1_noised, x2_noised, np.ones(N)]

U, s, vh = np.linalg.svd(B, full_matrices=False)
vh = np.asmatrix(vh)
U = np.asmatrix(U)
v = vh.H

inv_s = np.hstack([1 / s[ :rank_B], np.zeros(col_B - rank_B)])
inv_s = np.diag(inv_s)
pseudo_inverse_B = v * inv_s * U.H
u = pseudo_inverse_B * b
print('u:')
print(u)
print('Least-squares solution by NumPy:')
print(np.linalg.lstsq(B, b, rcond=-1)[0])

x0 = - u[0] / 2
y0 = - u[1] / 2
r0 = np.ma.sqrt((u[0] ** 2 + u[1] ** 2 / 4) - u[2]).data
circle_center = (x0, y0)

fig, ax = plt.subplots()
ax.add_patch(plt.Circle(circle_center, r0, color='red', Fill = False, linewidth=1.5))
ax.plot(x1, x2, 'g-', x1_noised, x2_noised, 'b.')
ax.set_aspect('equal', adjustable='datalim')
ax.plot()
plt.legend(['generated', 'disturbed', 'fitted'], loc='best')
plt.show()