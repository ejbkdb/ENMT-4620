import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import minimize_scalar




def obj(x):
    return 5 - x + 0.45 * x**2 -0.08**3 +0.005*x**4

# def obj(x):
#     return 5 - 20*x + 0.45 * x**2 -0.08**3

# res = minimize_scalar(obj, bounds = (-100,100), method= 'bounded')
# print('scipy_min=',res.x)

def nextguess(x1, x2, x3, xstar):
    x = np.matrix([[x1],[x2],[x3]])
    max_pos = np.argmax(np.asarray(abs(xstar[0] - x)))

    if max_pos == 0:
        return x2,x3, xstar[0]
    if max_pos == 1:
        return x1,xstar[0],x3
    if max_pos == 2:
        return xstar[0],x1,x2,
def p(x,C):
    C = np.squeeze(np.asarray(C))
    return C[0]*x**2 + C[1]*x + C[2]


x1 = 25
x2 = 50
x3 = 75


xstar=[]
eq = []


for i in range (1,20):


    F = np.matrix([[obj(x1)],
                   [obj(x2)],
                   [obj(x3)]])

    X = np.matrix([[x1**2, x1, 1],
                   [x2**2, x2, 1],
                   [x3**2, x3, 1]])

    C = np.matmul(X.I,F)

    eq.insert(0,C)

    xstar.insert(0,C.item(1)/2/C.item(0))

    x1,x2,x3 = nextguess(x1,x2,x3,xstar)

    if len(xstar) > 1:
        if abs(obj(xstar[0]) - obj(xstar[1])) < 0.5:
            break




