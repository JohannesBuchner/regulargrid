from regulargrid.interpn import interpn
def test_interpn_grid():
	for x in [0, 1, 0.5]:
		for y in [0, 1, 0.5]:
			print x, y, interpn([0,1], [0,1], [[1, 2], [3, 4]], x, y, method='linear')
	
if __name__ == '__main__':
	numpy.random.seed(0)
	limits = [(-10,10), (-3,3)]
	breaks = [numpy.array([lo] + sorted(numpy.random.uniform(lo,hi, size=50)) + [hi]) 
		for lo,hi in limits]
	
	npoints = numpy.product([len(b) for b in breaks])
	inputvalues = []
	values = []
	for x in breaks[0]:
		vx = []
		for y in breaks[1]:
			z = numpy.random.normal(0, 1)**2.
			z = numpy.exp(-0.5 * ((x - -3)**2 + (y - 1)**2.))
			inputvalues.append([x, y, z])
			vx.append(z)
		values.append(vx)
	
	outputvalues = []
	for i in range(1000):
		x = [numpy.random.uniform(lo, hi) for lo,hi in limits]
		z = interpn(*(breaks + [values] + x), method='linear')
		outputvalues.append(x + [z])
	numpy.savetxt("interpn_test_input.txt", inputvalues)
	numpy.savetxt("interpn_test_output.txt", outputvalues)
	

