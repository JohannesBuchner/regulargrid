from scipy.interpolate import interp1d

def interpn(*args, **kw):
	"""Interpolation on N-D. 

	ai = interpn(x, y, z, ..., a, xi, yi, zi, ...)
	where the arrays x, y, z, ... define a rectangular grid
	and a.shape == (len(x), len(y), len(z), ...)
	"""
	method = kw.pop('method', 'cubic')
	if kw:
		raise ValueError("Unknown arguments: " % kw.keys())
	nd = (len(args)-1)//2
	if len(args) != 2*nd+1:
		raise ValueError("Wrong number of arguments")
	q = args[:nd]
	qi = args[nd+1:]
	a = args[nd]
	for j in range(nd):
		a = interp1d(q[j], a, axis=j, kind=method)(qi[j])
	return a

__doc__ = interpn.__doc__

