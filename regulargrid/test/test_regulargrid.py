from regulargrid.regulargrid import RegularGrid
import numpy

def test_regular_grid():
	rg = RegularGrid([(0,1), (0,1)], numpy.array([[], []]), numpy.array([[1, 2], [3, 4]]))
	for x in [0, 1, 0.5]:
		for y in [0, 1, 0.5]:
			print x, y, rg([x,y])
	
if __name__ == '__main__':
	numpy.random.seed(0)
	limits = [(-10,10), (-3,3)]
	breaks = [numpy.array(sorted(numpy.random.uniform(lo, hi, size=50))) for lo,hi in limits]
	
	npoints = numpy.product([len(b)+2 for b in breaks])
	inputvalues = []
	values = []
	for x in [limits[0][0]] + list(breaks[0]) + [limits[0][1]]:
		vx = []
		for y in [limits[1][0]] + list(breaks[1]) + [limits[1][1]]:
			z = numpy.random.normal(0, 1)**2.
			z = numpy.exp(-0.5 * ((x - -3)**2 + (y - 1)**2.))
			inputvalues.append([x, y, z])
			vx.append(z)
		values.append(vx)
		#print '    y', len(vx), len(breaks[1]), limits[1]
	#print '  x', len(values), len(breaks[0]), limits[0]
	values = numpy.array(values)
	print values.shape
	
	rg = RegularGrid(limits, breaks, values)
	outputvalues = []
	for i in range(1000):
		x = [numpy.random.uniform(lo, hi) for lo,hi in limits]
		outputvalues.append(x + [rg(x)])
	numpy.savetxt("regulargrid_test_input.txt", inputvalues)
	numpy.savetxt("regulargrid_test_output.txt", outputvalues)
	

