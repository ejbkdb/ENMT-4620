import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import minimize_scalar

def obj(x):
    return 5 - x + 0.45 * x**2 -0.08**3 +0.005*x**4

def xnew(xbase,deltax):
    newx = xbase+deltax
    if obj(newx) < obj(xbase):


        return xbase+deltax, deltax*1.2, 1.
    if obj(newx) > obj(xbase):
        return xbase - deltax, -0.5*deltax, 2.





xbase = 30.
deltax = 5.
x=[]
y=[]

for i in range(0,200):


    newx, deltax, result = xnew(xbase,deltax)
    xbase = newx

    print(xbase)
    x.append(xbase)
    y.append(obj(xbase))

