import numpy as np




from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# fig = plt.figure()
# ax = Axes3D(fig)
# # x = [0, 1, 1, 0]
# # y = [0, 0, 1, 1]
# # z = [0, 1, 0, 1]
#
# for combos in combo:
#     a,b,c = XYZ(combos)
#     verts = [list(zip(a, b, c))]
#     print(verts)
#     ax.add_collection3d(Poly3DCollection(verts), zs='z')
#     plt.show()












def obj(x,y,b=1):
    return np.sin(10*(x**2+y**2))/10
    # return np.sin(1*x)*np.cos(1*y) / .1
    # return -b*(x**2 + y**2)

# def obj(x,y,a,b,c,d):
#     z = (x**2/a**2)+(y**2/b**2)
#     return -(((x - b) / a) ** 2 + ((y - d) / c) ** 2) + 1.0


##### setup

# param = np.asarray([[-6,-6],[-5.07,-5.61],[-5.61,-5.08]])

# param = np.asarray([[6,6],[5.07,5.61],[5.61,5.08]])

param = np.asarray([[6,-6],[5.07,-5.61],[5.61,-5.08]])




# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))



############################################
def results(num_variables, parameter_array):
    result = np.zeros([num_variables+1,1])

    for i in range(0,num_variables+1):
        x = parameter_array[i][0]
        y = parameter_array[i][1]
        result[i] = obj(x,y)
    return result


# result_array = results(2,init)
#############################################
def find_worst(result_array):
    worst = np.argmin(result_array)
    return worst
# current_worst = find_worst(result_array)

############################################

def midpoint(num_variables,current_worst,parameter_array):
    parameters = parameter_array.copy()
    parameters[current_worst] = 0
    midPoint = np.zeros(num_variables)
    for j in range(0,num_variables):
             midPoint[j] = np.sum(parameters[:num_variables+1,j])/num_variables # number of rows = numvariables +1, you do this for each column

    return midPoint

# parameter_centroid = midpoint(2,current_worst,init)
#############################################

def newpoint(worst,centroid,parameter_array):

    parameters = parameter_array

    alpha =1
    old_x = parameters[worst][0]
    old_y = parameters[worst][1]

    centroid_x = centroid[0]
    centroid_y = centroid[1]

    new_x = centroid_x + alpha*(centroid_x-old_x)
    # print(new_x)
    new_y = centroid_y + alpha*(centroid_y-old_y)
    # print(new_y)
    parameters[worst][0] = new_x
    parameters[worst][1] = new_y
    # plt.plot(param,'o')
    # time.sleep(1.0)

    return parameters

def combinedata(result_array,parameter_array):
    results = result_array.copy()
    parameters = parameter_array.copy()

    combined = np.concatenate((parameter_array,result_array),axis=1)


    return combined

def XYZ(xyz_array):
    x_data = xyz_array[:,0]
    y_data = xyz_array[:,1]
    z_data = xyz_array[:,2]

    return x_data, y_data, z_data


def update(i):
    a,b,c = XYZ(combo[i])
    verts = [list(zip(a, b, c))]
    # print(verts)
    ax.add_collection3d(Poly3DCollection(verts, edgecolors='black', linewidths=1), zs='z')
    return

i = 0
combo = []
while (i<15):
    print(param)
    i=i+1
    result_array = results(2, param)
    combo.append(combinedata(result_array,param)) # get xyz array of points

    current_worst = find_worst(result_array)
    parameter_centroid = midpoint(2, current_worst, param)

    param = newpoint(current_worst,parameter_centroid,param)


################plotting start
x = np.linspace(-20, 20, 50)
y = np.linspace(-20, 20, 50)

X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# Z = obj(X,Y,a,b,c,d)
Z = obj(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
# plt.contour(X,Y,Z,10)


# fig = plt.figure()
# ax = p3.Axes3D(fig)

# ax.add_collection3d(Poly3DCollection(update_vert(combo[1]), edgecolors='black', linewidths=1), zs='z')
# plt.show()

# for i in range(0,len(combo))
line_ani = animation.FuncAnimation(fig,update, frames = len(combo),interval=500)
line_ani.save('basic_animation2.mp4', fps=1, extra_args=['-vcodec', 'libx264'])
plt.show()



# for combos in combo:
#     a,b,c = XYZ(combos)
#     verts = [list(zip(a, b, c))]
#     print(verts)
#     ax.add_collection3d(Poly3DCollection(verts, edgecolors='black', linewidths=1), zs='z')
#     plt.show()
#     time.sleep(1.0)