from regulargrid.interpn import interpn
import numpy
from numpy import sin, pi

x = numpy.linspace(0, 1, 8)
y = numpy.linspace(0, 1, 9)
z = numpy.linspace(0, 1, 10)

Z, Y = numpy.meshgrid(y, z)
X = numpy.array([[x]]).transpose()
X = Y * 0 + X
Y = X * 0 + Y
Z = X * 0 + Z
print X.shape, Y.shape, Z.shape
# ) * sin(Y*2*pi*3) * 
a = numpy.exp(-0.5 * (((X-0.3)/0.2)**2 + ((Y-0)/0.2)**2 * 0 + ((Z-0.6)/0.3)**2)) * (sin(Y*2*pi*3) + 1)
print a.shape, a.min(), a.max()
xv = numpy.linspace(0, 1, 33)
yv = numpy.linspace(0, 1, 33)
zv = numpy.linspace(0, 1, 33)

print 'evaluating'
values = []
for xi in xv:
	yvalues = []
	for yi in yv:
		zvalues = []
		for zi in zv:
			v = interpn(x, y, z, a, xi, zi, yi)
			#z = numpy.exp(-0.5 * (((xi-0.3)/0.2)**2 + ((yi-0.6)/0.3)**2))
			zvalues.append(v)
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
plt.savefig('test_interpnd.pdf')
plt.close()


