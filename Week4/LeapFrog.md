# Leapfrog Algorithm Writeup

This writeup with step through the code used to implement a 1D interpreation of Leapfrog algorithm

Complete code can be found here [link to code:](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/leapfrog_1D.py)

### Equation Definition:
  - to utilize simply pass the x-variable to the function. Function will return y value.
```python
def obj(x):
return 5 - x + 0.45 * x**2 -0.08**3 +0.005*x**4
```

### Initial Setup:
- To initialize Leapfrog you first have to define the interval you want to generate points over and the amount of 'players' you will assign. Interval is X, Y is the players. In generate_pts, players is set to zero, while interval is randomly selected between the specified range
```python

def generate_pts(interval=20, players = 20):
    pts = np.zeros((players,2))
    for i in range(0,players):
      pts[i,0] = np.random.uniform(-interval,interval)
return pts


```

### Generating Y values
- After the random interval pts have been selected and y has been initialized with zeros. I populate the y values by utilizing the objective function
```python
def generate_y(queue):
    for i in range(0,len(queue)):
        queue[i,1] = obj(queue[i,0])
return queue
```

### New X function
- This function is used to create the new value of x. this equation is embedded in another function that that performs the swapping out the worst value
- Per the leapfrog algorithm it assigns a random number between 0 and 1 to help randomize the new x value

```python
def xnew(xbest,xworst_old):
    random = np.random.uniform(0,1)
return xbest + random*(xbest-xworst_old)
```

### Swap Worst Function
- Returns the best and worst values from the current queue. Feeds best and worst value into the xnew function and returns a new queue to be processed again.
```python
def swap_worst(queue):
    x = queue[:,0]
    y = queue[:,1]
    # list = np.argsort(queue,axis=0)
    best = x[np.argmin(y)]
    worst = x[np.argmax(y)]
    x[np.argmax(y)] = xnew(best,worst)
return np.column_stack((x,y))
```


### Exit Condition:
- if the standard deviation between y and x values are <0.5 the function is considered converged and exits.
- a 20 player optimization takes ~90 iterations to converge
- a 100 player optimization takes ~500 iterations to converge
```python
    if np.std(points[:,1]) and np.std(points[:,0]) < .05:

        print(i)
break
       
```

### Functions implemented:
- Shows how the functions were implemented into a loop with exit criteria

```python
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

```

### Results:

- Graph OF vs. DV

![OF vs DV](https://github.com/ejbkdb/ENMT-4620/blob/master/Week%203/004_Objective_Function.png "OF vs DV")

- All points Leapfrog, 20 players, -20:20 interval
![All points](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/leapfrog_xy_output.png "All points")


- Convergence of X

![X converg](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/leapfrog_x_converg.png "X convergence")

- Convergence of Y

![y Converg](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/leapfrog_y_converg.png "Y convergence")

- Video of Leapfrog convergence (click image):

[![Video of Leapfrog convergence](https://img.youtube.com/vi/0_wypML0DjQ/0.jpg)](https://www.youtube.com/watch?v=0_wypML0DjQ)

### Result Check:

Utilized scipy.optimize.minimize_scalar(OF) results = 1.08, Golden section result = 1.08. Results checked out!
