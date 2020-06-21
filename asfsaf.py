d = {
    i:ord(i) for i in ['a', 'b', 'c', 'd', 'e']
}

import pandas as pd

a = {
    'a': pd.Series([1,2,3], index = ['1', '2', '3']),
    'b': {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
}

obj = pd.DataFrame(a)
obj

#-------------------Numpy-----------------------------

"""
-- An array can be indexed by a tuple of nonnegative integers,
by booleans, by another array, or by integers.

-- Rank - Number of dimensions/axes(plural of axis) (dimensions are like in how many
directions one can walk)

-- Shape - A tuple of integers giving the size of the array along
each dimension (it is like how many blocks one can walk upto in a dimension)



"""

import numpy as np
a = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

b = np.ones((2,3))
b

c = np.empty((2,3,4))
c

d = np.linspace(2,18,4)
d

l = [
    [1,2,3],
    [2,1,4],
    [12,0,23]
]

sorted(l, key = lambda i: i[1]+1)

a = np.array([
    [
        [5,6],
        [3,8]
    ],
    [
        [1,2],
        [7,4]
    ]
])

a = np.array([[i, i+1, i+2, i+3] for i in range(1, 13, 4)])
np.arange(1,13,1).reshape((3,4))

list_coordinates = list(zip(a[0], a[1]))

for coord in list_coordinates:
    print(coord)

np.hsplit(a, (2,3))

l = [1,2,3,4]
l[:45]

a[0,1] = 23
b = a[:]
b[0,1] = 54
b
a
a = np.array([[[
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
],
[
    [
        [9,10],
        [11,12]
    ],
    [
        [13,14],
        [15,16]
    ]
]]])

a.sum(axis=0)

a = np.array([i for i in range(1, 5)])
a.prod()

a = np.ndarray([[1,2], [3,4]])

a = np.arange(1, 13).reshape((3,4))

np.flip(a, axis = 1)

import pandas as pd

df = pd.DataFrame(a)

#--------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fig = plt.figure()

ax = Axes3D(fig)

X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)

X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'viridis')
plt.show()

#----------------------------------------------------

x = np.arange(10)
x.shape = (2,5)

y = np.arange(35).reshape(5,7)
b = y > 20
y[b]

y[b[:,5][np.newaxis, :].T]

b[:,5][np.newaxis, :].T

x = np.arange(30).reshape(2,3,5)

b = np.array([True, False])
x[b]


import numpy as np

a = np.arange(35).reshape(5,7)

a[np.array([1,2,3]), np.array([1,2,3])]