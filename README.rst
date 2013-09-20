Regular Grid Multivariate linear interpolation
===============================================

Non-recursive implementation of linear interpolation on `regular grids <https://en.wikipedia.org/wiki/Regular_grid>`_.

* Cartesian grid **regulargrid.cartesiangrid.CartesianGrid** (equal spacing between points)

	Uses very fast implementation based on scipy.ndimage.map_coordinates

	Example::

		# create a 3-dimensional cartesian grid:
		limits = [(0, 1), (0, 1), (0, 1)]
		x = numpy.linspace(0, 1, 8)
		y = numpy.linspace(0, 1, 9)
		z = numpy.linspace(0, 1, 10)

		Z, Y = numpy.meshgrid(z, y)
		X = numpy.array([[x]]).transpose()

		# our grid values
		values = X**2 + Y - Z

		from regulargrid.cartesiangrid import CartesianGrid
		# does linear interpolation
		grid = CartesianGrid(limits, values)

		# interpolate for one point
		print grid([0.1], [0.5], [0.3])
		# interpolate many
		print grid([0.1, 0.3], [0.5, 0.5], [0.3, 0.2])

* Regular grid **regulargrid.regulargrid.RegularGrid** (unequal spacing between points)
	

References:

   * Trilinear interpolation. (2013, January 17). In Wikipedia, The Free Encyclopedia. Retrieved 01:28, February 27, 2013, from http://en.wikipedia.org/w/index.php?title=Trilinear_interpolation&oldid=533448871 
   * Weiser, Alan, and Sergio E. Zarantonello. "A note on piecewise linear and multilinear table interpolation in many dimensions." MATH. COMPUT. 50.181 (1988): 189-196. http://www.ams.org/journals/mcom/1988-50-181/S0025-5718-1988-0917826-0/S0025-5718-1988-0917826-0.pdf


