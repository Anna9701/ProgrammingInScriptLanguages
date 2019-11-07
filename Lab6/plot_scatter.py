import numpy as np
import matplotlib.pyplot as plt


data = np.array([10, 12, 7, 5, 6])

#plt.plot(range(len(data)), data, color = "g", ls = "-.", lw = "2", 
#         marker = "o", markersize = 10, 
#         markerfacecolor = "r", markeredgecolor = "b", markeredgewidth = 4)
#         markerfacecolor = "r", markeredgecolor = "b", markeredgewidth = 4)
#plt.plot(np.arange(len(data)), data + 1, color = "g", marker = "1", markersize = 15)
#plt.scatter(np.arange(len(data)), data + 1, color = "g", marker = "1", markersize = 15)

linestyles = ["-", "--", ":", "-."]
for j, i in enumerate(np.arange(-2, 2)):
  plt.plot(np.arange(len(data)), data + i, 
           marker = str(j + 1), markersize = 15, lw = 2, ls = linestyles[j], 
           label = "series " + str(j + 1))
plt.legend(ncol = 2)
plt.show()
