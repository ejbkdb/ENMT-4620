import matplotlib.pyplot as plt
import numpy as np

#Function
def func(x):
    return 5 - x + 0.45 * x ** 2 - 0.08 ** 3 + 0.005 * x ** 4


##########################################
from scipy.optimize import minimize_scalar

res = minimize_scalar(func, bounds = (-20,20), method= 'bounded')
res.x
#########################################


#Generate X&Y values for plotting
steps = range(-100,100)
b = []
for step in steps:
    b.append(func(step))

plt.plot(steps,b)


x_up = 20
x_lo = -20


golden_ratio = ((np.sqrt(5)-1)/2)
d = golden_ratio*(x_up-x_lo)
new_x_up = x_lo + d
new_x_lo = x_up - d

fig = plt.figure()

XLO = []
XHI = []

for i in range (0,100):
    if func(new_x_lo) < func(new_x_up):
        x_up = new_x_up
        new_x_up = new_x_lo

        d = golden_ratio*(x_up-x_lo)
        new_x_lo = x_up-d
        XLO.insert(0,new_x_lo)
        print('one_', new_x_up,new_x_lo)
    if func(new_x_lo) > func(new_x_up):
        x_lo= new_x_lo
        new_x_lo = new_x_up
        d = golden_ratio*(x_up - x_lo)
        new_x_up = x_lo + d
        XHI.insert(0,new_x_up)

        print('two_', new_x_up,new_x_lo)


    plt.plot(x_lo,func(x_lo),'or')
    plt.show()
    plt.plot(x_up,func(x_up),'ob')
    plt.show()


    if len(XLO) and len(XHI) > 1:
        if abs(XLO[0] - XLO[1]) and abs(XHI[0] - XHI[1])  < 0.1:
            break

