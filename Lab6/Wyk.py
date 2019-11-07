import numpy as np
import math as math
import time as t



def numpy_sieve(n: int):
    tab = np.ones(n, dtype=bool)
    tab[0:2] = False
    for i in range (2, math.sqrt(n).__int__()):
        if tab[i]:
            for j in range (i**2, n, i):
                tab[j] = False
    return np.where(tab)


start = t.time()
x = numpy_sieve(5000000)
end = t.time()
print(end - start)