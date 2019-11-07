import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize = (7, 3.5))
plt.plot(range(5), [x * 2 - 1 for x in range(5)])
fig.savefig("simple_graph.jpg", dpi = 120, facecolor = "#20ff77")
