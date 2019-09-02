import numpy as np
import scipy
import scipy.linalg
import time
import matplotlib.pyplot as plt

eps = 1.0 / np.power(10, 16)

def ma_ex(xarray):
    n = len(xarray)
    A = []
    for i in range(n):
        line_i = [xarray[i] ** j for j in range(n - 1, -1, -1)]
        A.append(line_i)
    return np.array(A)


xarray = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]
A = ma_ex(xarray)
left_outflow = np.array([[1.18087], [0.439936], [0.246752], [0.0546872], [0.0277186], [0.00560254]])
right_outflow = np.array([[1.81913], [2.56006], [2.75325], [2.94531], [2.97228], [2.99439]])

lin_left_outflow = np.array([[1.18099],[0.439948],[0.246913],[0.0547608],[0.0277583],[0.00561366]])
lin_right_outflow = np.array([[1.81997],[2.56141],[2.7547],[2.94687],[2.97385],[2.99598]])
v1 = scipy.linalg.solve(A, lin_left_outflow)
v2 = scipy.linalg.solve(A, lin_right_outflow)


def f(x, v1):
    return x ** 5 * v1[0][0] + x ** 4 * v1[1][0] + x ** 3 * v1[2][0] + x ** 2 * v1[3][0] + x * v1[4][0] + v1[5][0]

xarray = np.linspace(0,0.5,100)
yarray = [f(xarray[i],v2) for i in range(len(xarray))]
fig = plt.figure(1)
plt.plot(xarray,yarray)
plt.savefig("LinPlotMixedExtrRight.png")
plt.grid()
plt.xlabel("Permeabilität")
plt.ylabel("RightOutflow")
plt.grid(True)
plt.savefig("19/linrechts.png")

xarray = np.linspace(0,0.5,100)
yarray = [f(xarray[i],v1) for i in range(len(xarray))]
fig = plt.figure(2)
plt.plot(xarray,yarray)
plt.grid()
plt.xlabel("Permeabilität")
plt.ylabel("LeftOutflow")
plt.grid(True)
plt.savefig("19/linlinks.png")

v1 = scipy.linalg.solve(A, left_outflow)
v2 = scipy.linalg.solve(A, right_outflow)

xarray = np.linspace(0,0.5,100)
yarray = [f(xarray[i],v2) for i in range(len(xarray))]
fig = plt.figure(3)
plt.plot(xarray,yarray)
plt.grid()
plt.xlabel("Permeabilität")
plt.ylabel("RightOutflow")
plt.grid(True)
plt.savefig("19/mixrechts.png")

xarray = np.linspace(0,0.5,100)
yarray = [f(xarray[i],v1) for i in range(len(xarray))]
fig = plt.figure(4)
plt.plot(xarray,yarray)
plt.grid()
plt.xlabel("Permeabilität")
plt.ylabel("LeftOutflow")
plt.grid(True)
plt.savefig("19/mixlinks.png")