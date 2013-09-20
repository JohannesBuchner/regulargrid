import numpy
import itertools

class CartesianGrid(object):
	"""
	Linear Multivariate Cartesian Grid interpolation in arbitrary dimensions
	This is a regular grid with equal spacing.
	"""
	def __init__(self, limits, values):
		self.values = values
		self.limits = limits
		self.highestindex = numpy.array(self.values.shape) - 1
	
	def __call__(self, *coords):
		"""
		interpolation at coordinates, which are already [0,size)
		"""
		# find relevant edges between which coords is situated
		#print coords,
		for c in coords:
			assert numpy.shape(c) != (), ('need array of coordinates, not just one', coords)
		coords = [(c - lo) * (n - 1) / (hi - lo) for (lo, hi), c, n in zip(self.limits, coords, self.values.shape)]
		
		indices = numpy.floor(coords).astype(int)
		for j, i in enumerate(indices):
			mask = i == self.highestindex[j]
			indices[j][mask] = self.highestindex[j] - 1
		
		norm_distances = numpy.asarray(coords) - indices
		neg_norm_distances = 1 - norm_distances
		edges = numpy.array([[i, i + 1] for i in indices])
		#print edges.shape
		#edges = edges.reshape([edges.shape[0]] + list(edges.shape)[2:])
		
		# find relevant values
		# each i and i+1 represents a edge
		value = 0.
		#print 'edges', edges.shape, edges
		for edge_indices in itertools.product(*edges):
			#print 'ei', edge_indices, 'indices', indices
			weight = numpy.where(edge_indices == indices, neg_norm_distances, norm_distances)
			
			#assert (edge_indices == indices).shape == numpy.asarray(edge_indices).shape
			#assert (edge_indices == indices).shape == indices.shape
			#print 'weight', weight.shape, weight.prod(axis=0).shape, weight
			#print 'edges', numpy.asarray(edge_indices).shape, 'values', self.values[edge_indices], 
			value += self.values[edge_indices] * weight.prod(axis=0)
			#print 'weights:', edge_indices, self.values[edge_indices], weight
		#print value
		return value

__doc__ = CartesianGrid.__doc__

