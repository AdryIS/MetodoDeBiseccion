#Ejemplo del paracaidas
import math
import numpy as np
import matplotlib.pyplot as plt


def fun(c):
    return (667.38 / c) * (1 - math.exp(-0.1484 * c)) - 40


arrayLen = 100
cIni = 0
cEnd = 30
cArray = np.linspace(cIni, cEnd, arrayLen)
fcArray = np.zeros(arrayLen)

for i in range(arrayLen):
    fcArray[i] = fun(cArray[i])

plt.plot(cArray, fcArray)
plt.grid()

c0 = 10
c1 = 20
maxIter = 100
itera = 0

for i in range(maxIter):
    itera += 1
    fc0 = fun(c0)
    fc1 = fun(c1)
    if fc0 * fc1 > 0:
        print("No hay raiz en este rango")
        break
    cr = (c0 + c1) / 2
    fcr = fun(cr)
    if fc0 * fcr < 0:
        c1 = cr
    else:
        c0 = cr
    if abs(fcr) < 0.00001:
        break

print("La raiz es %.5f" % c0)
print("Con iteraciones %i" % itera)
