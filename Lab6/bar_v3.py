import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N) 
width = 0.35    

p1 = plt.bar(ind,         menMeans,   width, color = "r")
p2 = plt.bar(ind + width, womenMeans, width, color = "y")

plt.ylabel("Scores")
plt.title("Scores by group and sex")
plt.xticks(ind + width / 2, ("G1", "G2", "G3", "G4", "G5"))
#plt.yticks(np.arange(0, 41, 10))
plt.legend((p1[0], p2[0]), ("Men", "Women"))

plt.show()
