# Heuristic Algorithm Writeup

This writeup with step through the code used to implement a 1D interpreation of Heuristic Algorithm

Complete code can be found here [link to code:](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/heuristic.py)

### Equation Definition:
  - to utilize simply pass the x-variable to the function. Function will return y value.
```python
def obj(x):
return 5 - x + 0.45 * x**2 -0.08**3 +0.005*x**4
```

### Initial Setup:
- To initialize heuristic search you have to initialize a starting point and a st
```python

xbase = 30.
deltax = 5.
x=[]
y=[]


```

### Generating new X values
- To generate new values I followed the pseudocode referenced in class textbook. utilizing simple logic if the value is an improvement deltax is increased by 1.2 times and a new point is assigned. If the point is worse deltax X is decreased by -0.5 deltax causing the point to retreat backwards

```python
def xnew(xbase,deltax):
    newx = xbase+deltax
    if obj(newx) < obj(xbase):


        return xbase+deltax, deltax*1.2, 1.
    if obj(newx) > obj(xbase):
        return xbase - deltax, -0.5*deltax, 2.

```

### Exit Condition:
- I did not assign an exit condition for this algorithm. If I would assign an exit condition if would look at hte previous values and determine when the x value stopped improving.



### Functions implemented:
- Shows how the functions were implemented into a loop with exit criteria

```python
for i in range(0,200):


    newx, deltax, result = xnew(xbase,deltax)
    xbase = newx


```

### Results:

- Graph OF vs. DV

![OF vs DV](https://github.com/ejbkdb/ENMT-4620/blob/master/Week%203/004_Objective_Function.png "OF vs DV")

- All iterations Heuristic
- You can see oscillation once the algorithm gets close to minimum
![All points](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/heuristic_xy_output.png "All points")


- Convergence of X

![X converg](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/heuristic_x_converg.png "X convergence")

- Convergence of Y

![y Converg](https://github.com/ejbkdb/ENMT-4620/blob/master/Week4/heuristic_y_converg.png "Y convergence")


### Result Check:

Utilized scipy.optimize.minimize_scalar(OF) results = 1.08, Golden section result = 1.08. Results checked out!
