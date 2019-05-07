import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.pyplot as plt
import numpy as np
import  time
from scipy.optimize import minimize_scalar

from matplotlib.animation import FuncAnimation,FFMpegFileWriter


def obj(x):
    return 5 - x + 0.45 * x**2 -0.08**3 +0.005*x**4

def xnew(xbest,xworst_old):
    random = np.random.uniform(0,1)
    return xbest + random*(xbest-xworst_old)

def generate_pts(interval=20, players = 20):
    pts = np.zeros((players,2))
    for i in range(0,players):
      pts[i,0] = np.random.uniform(-interval,interval)
    return pts

def swap_worst(queue):
    x = queue[:,0]
    y = queue[:,1]
    # list = np.argsort(queue,axis=0)
    best = x[np.argmin(y)]
    worst = x[np.argmax(y)]
    x[np.argmax(y)] = xnew(best,worst)
    return np.column_stack((x,y))

def generate_y(queue):
    for i in range(0,len(queue)):
        queue[i,1] = obj(queue[i,0])
    return queue


def animate(i):
    global x,y
    ax1.clear()
    ax1.plot(x[i],y[i],'o')

points = generate_pts(players=20)
int_points = points

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x = []
y = []

for i in range(2000):
    x.append(points[:,0])
    y.append(points[:,1])

    points = generate_y(points)
    points = swap_worst(points)

    if np.std(points[:,1]) and np.std(points[:,0]) < .05:

        print(i)
        break

x = np.asarray(x)
y = np.asarray(y)



ani = animation.FuncAnimation(fig,animate,interval=500)
plt.show()


