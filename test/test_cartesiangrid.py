from regulargrid.cartesiangrid import CartesianGrid
import numpy
from numpy import sin, pi
import sys

x = numpy.linspace(0, 1, 8)
y = numpy.linspace(0, 1, 9)
z = numpy.linspace(0, 1, 10)

Z, Y = numpy.meshgrid(z, y)
X = numpy.array([[x]]).transpose()
print X.shape, Y.shape, Z.shape
X = X + (Y) * 0
Y = Y + (X) * 0
Z = Z + (X) * 0
print X.shape, Y.shape, Z.shape

# choose one point, then set neighboring ones
#       1        
#    1110111
#       1
#       1

a = (X + Y + Z) * 0

i0, j0, k0 = (3, 3, 3)

a[i0, j0, k0] = 10
# first, fill one dimension at origin
for i in range(1, len(x)):
	if i0 - i >= 0:
		a[i0 - i, j0, k0] = a[i0 - i + 1, j0, k0] * 0.9
	if i0 + i < len(x):
		a[i0 + i, j0, k0] = a[i0 + i - 1, j0, k0] * 0.9

del i
# then, fill third dimension next to this line
for k in range(1, len(z)):
	if k0 - k >= 0:
		a[:, j0, k0 - k] = a[:, j0, k0 - k + 1] * 0.9
	if k0 + k < len(z):
		a[:, j0, k0 + k] = a[:, j0, k0 + k - 1] * 0.9
del k
# then, fill second dimension next to this plane
for j in range(1, len(y)):
	if j0 - j >= 0:
		a[:, j0 - j, :] = a[:, j0 - j + 1, :] * 0.9
	if j0 + j < len(y):
		a[:, j0 + j, :] = a[:, j0 + j - 1, :] * 0.9
del j



xv = numpy.linspace(0, 1, 33)
yv = numpy.linspace(0, 1, 33)
zv = numpy.linspace(0, 1, 33)

xi = numpy.array([0.5, 0.3]) # .transpose()
#xi = 0.5
yi = xi
zi = xi
grid = CartesianGrid([(0, 1)] * 3, a)
print grid(xi, yi, zi)

from time import time as time
start = time()
grid(*[numpy.random.uniform(0, 1, 100000) for _ in range(3)])
print '10000 random evals:', time() - start
start = time()
for i in range(100):
	grid(*[numpy.random.uniform(0, 1, 10000) for _ in range(3)])
print '10x1000 random evals:', time() - start

print 'evaluating'
values = []
for xi in xv:
	yvalues = []
	for yi in yv:
		zvalues = grid(xi + zv*0, yi + zv*0, zv)
		
		"""zvalues = []
		for zi in zv:
			#v = interpn(x, y, z, a, xi, zi, yi)
			v = grid(numpy.array([xi]), 
				numpy.array([yi]), 
				numpy.array([zi]))
			#z = numpy.exp(-0.5 * (((xi-0.3)/0.2)**2 + ((yi-0.6)/0.3)**2))
			zvalues.append(v)"""
		#print zvalues.shape, zv.shape
		yvalues.append(zvalues)
	values.append(yvalues)
values = numpy.array(values)
print 'plotting'

import matplotlib.pyplot as plt
def imshow(arr, title):
	plt.title(title)
	plt.imshow(arr, extent=(0, 1, 1, 0), vmin=0, vmax=a.max(), interpolation='none')
	plt.colorbar()

plt.figure(figsize=(10,10))
plt.subplot(3, 2, 1)
imshow(a[:,:,0], title='a3')
plt.subplot(3, 2, 2)
imshow(values[:,:,0], title='v3')
plt.subplot(3, 2, 3)
imshow(a[:,0,:], 'a2')
plt.subplot(3, 2, 4)
imshow(values[:,0,:], 'v2')
plt.subplot(3, 2, 5)
imshow(a[0,:,:], 'a1')
plt.subplot(3, 2, 6)
imshow(values[0,:,:], 'v1')
plt.savefig('test_neighbors.pdf')
plt.close()


