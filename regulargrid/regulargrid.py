import numpy
import itertools

class RegularGrid(object):
	"""
	Linear Multivariate Regular Grid interpolation in arbitrary dimensions
	"""
	def __init__(self, limits, breaks, values):
		assert len(breaks) == len(limits), [len(breaks), len(limits)]
		
		gridall = []
		for l, b in zip(limits, breaks):
			assert b == [] or numpy.all(numpy.asarray(b) > l[0]), [b, l[0]]
			assert b == [] or numpy.all(numpy.asarray(b) < l[1]), [b, l[1]]
			grid = numpy.array([l[0]] + list(b) + [l[1]])
			gridall.append(grid)
			assert numpy.all(grid[1:] > grid[:-1]), 'breaks need to be ascending'
		self.grid = gridall
		assert values.shape == tuple([len(b)+2 for b in breaks]), [
			values.shape, [len(b)+2 for b in breaks]]
		#assert len(values) == numpy.product([len(b)+2 for b in breaks])
		self.values = values
	
	def __call__(self, *coords):
		"""
		interpolation at coordinates
		"""
		# find relevant edges between which coords is situated
		indices = []
		# compute distance to lower edge in unity units
		norm_distances = []
		for coord, breaks in zip(coords, self.grid):
			i = numpy.searchsorted(breaks, coord) - 1
			if i == -1:
				assert coord == breaks[0], (coord, breaks[0])
				# got the last break point, but we don't want that
				i = 0

			indices.append(i)
			norm_distances.append((coord - breaks[i]) / (breaks[i+1] - breaks[i]))
		
		# find relevant values
		# each i and i+1 represents a edge
		edges = itertools.product(*[[i, i+1] for i in indices])
		value = 0.
		for edge_indices in edges:
			#j = 0 # addressing of grid
			weight = 1.
			#for ei, i, breaks, yi in zip(edge_indices, indices, self.grid, y):
				#j = j * len(breaks) + ei
			for ei, i, yi in zip(edge_indices, indices, norm_distances):
				weight *= (1 - yi) if ei == i else yi
			value += self.values[edge_indices] * weight
		return value

__doc__ = RegularGrid.__doc__

