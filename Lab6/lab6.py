import numpy as np
import numpy.ma as ma
import numpy.lib.recfunctions as rf
import matplotlib.pyplot as plt


def zad1():
    mu, sigma = 100, 15
    s = np.random.normal(mu, sigma, 64).astype(int).reshape((8, 8))

    print(s)

    fs = np.array(s)

    for i in range(1, s.shape[0] - 1):
        for j in range(1, s.shape[1] - 1):
            fs[i, j] = s[i-1, j-1] + s[i-1, j] + s[i-1, j+1] + s[i, j-1] + s[i, j] + s[i, j+1] + s[i+1, j-1] + s[i+1, j] + s[i+1, j+1]
            fs[i, j] /= 9

    print(fs)

def zad2():
    tab = np.array([3, 5, -52, -4, 24, 15, 17, 3, -20, -11, 33, 44]).reshape((3, 4))
    a = tab < -10
    b = tab > 15
    m = a | b
    masked_tab = ma.array(tab, mask=m)
    row_means = masked_tab.mean(1)
    print(row_means)

def zad3():
    rectangles = [("R1", 5, 4.5), ("Grubas", 11, 3), ("Inny", 4, 6), ("Chudy", 3, 8),
       ("Kwadrat 1", 5, 5), ("Kwadrat 2", 4.5, 4.5)]
    t = np.dtype([("name", 'S10'), ("width", np.int), ("height", np.float)])
    a = np.array(rectangles, dtype=t)

    t2 = np.dtype([("name", 'S10'), ("width", np.int), ("height", np.float), ("area", np.float)])
    r = []
    for i in range(0, len(rectangles)):
        r.append(tuple([a[i]["name"], a[i]["width"], a[i]["height"], a[i]["width"] * a[i]["height"]]))
    a2 = np.array(r, dtype=t2)
    temp = np.sort(a2, order=["area", "name"])
    for rectangle in temp:
        print("Width: " + str(rectangle["width"]) + " Height:" + str(rectangle["height"]) + " Name:" + str(rectangle["name"]))


data = np.array(np.recfromcsv("imiona.csv", delimiter = ';'))
kids_in_year = dict()

for entry in data:
    year = entry['rok']
    if year in kids_in_year:
        kids_in_year[year] += entry['liczba']
    else:
        kids_in_year[year] = entry['liczba']

x = list(kids_in_year.keys())
y = list(kids_in_year.values())



plt.plot(x[2:], y[2:], "g-")
plt.show()