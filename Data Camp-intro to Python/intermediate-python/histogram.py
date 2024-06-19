#	• Viz used to see distribution of variables
	# • Steps to creating it
	# 	○ Draw a number line
	# 	○ Place the # data pts in each bin 
	# 	○ Draw a bar - the height = # data pts that are in the bin
	# • For Gaussian distributions, most of the data pts lie in the middle

import matplotlib.pyplot as plt
help(plt.hist)

# hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)


#     Plot a histogram.

#     Compute and draw the histogram of *x*.  The return value is a tuple   
#     (*n*, *bins*, *patches*) or ([*n0*, *n1*, ...], *bins*, [*patches0*,  
#     *patches1*, ...]) if the input contains multiple data.  See the       
#     documentation of the *weights* parameter to draw a histogram of       
#     already-binned data.

#     Multiple data can be provided via *x* as a list of datasets
#     of potentially different length ([*x0*, *x1*, ...]), or as
#     a 2D ndarray in which each column is a dataset.  Note that
#     the ndarray form is transposed relative to the list form.

#     Masked arrays are not supported.

#     The *bins*, *range*, *weights*, and *density* parameters behave as in 
#     `numpy.histogram`.

#     Parameters
#     ----------
#     x : (n,) array or sequence of (n,) arrays
#         Input values, this takes either a single array or a sequence of   
#         arrays which are not required to be of the same length.

#     bins : int or sequence or str, default: :rc:`hist.bins`
#         If *bins* is an integer, it defines the number of equal-width bins
#         in the range.

#         If *bins* is a sequence, it defines the bin edges, including the  
#         left edge of the first bin and the right edge of the last bin;    
#         in this case, bins may be unequally spaced.  All but the last     
#         (righthand-most) bin is half-open.  In other words, if *bins* is::

#             [1, 2, 3, 4]

#         then the first bin is ``[1, 2)`` (including 1, but excluding 2) and        the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which        *includes* 4.

#         If *bins* is a string, it is one of the binning strategies        
#         supported by `numpy.histogram_bin_edges`: 'auto', 'fd', 'doane',  
#         'scott', 'stone', 'rice', 'sturges', or 'sqrt'.

#     range : tuple or None, default: None
#         The lower and upper range of the bins. Lower and upper outliers   
#         are ignored. If not provided, *range* is ``(x.min(), x.max())``.  
#         Range has no effect if *bins* is a sequence.

#         If *bins* is a sequence or *range* is specified, autoscaling      
#         is based on the specified bin range instead of the
#         range of x.

#     density : bool, default: False
#         If ``True``, draw and return a probability density: each bin      
#         will display the bin's raw count divided by the total number of   
#         counts *and the bin width*
#         (``density = counts / (sum(counts) * np.diff(bins))``),
#         so that the area under the histogram integrates to 1
#         (``np.sum(density * np.diff(bins)) == 1``).

#         If *stacked* is also ``True``, the sum of the histograms is       
#         normalized to 1.

#     weights : (n,) array-like or None, default: None
#         An array of weights, of the same shape as *x*.  Each value in     
#         *x* only contributes its associated weight towards the bin count  
#         (instead of 1).  If *density* is ``True``, the weights are        
#         normalized, so that the integral of the density over the range    
#         remains 1.

#         This parameter can be used to draw a histogram of data that has   
#         already been binned, e.g. using `numpy.histogram` (by treating each        bin as a single point with a weight equal to its count) ::        

#             counts, bins = np.histogram(data)
#             plt.hist(bins[:-1], bins, weights=counts)

#         (or you may alternatively use `~.bar()`).

#     cumulative : bool or -1, default: False
#         If ``True``, then a histogram is computed where each bin gives the
#         counts in that bin plus all bins for smaller values. The last bin 
#         gives the total number of datapoints.

#         If *density* is also ``True`` then the histogram is normalized such        that the last bin equals 1.

#         If *cumulative* is a number less than 0 (e.g., -1), the direction 
#         of accumulation is reversed.  In this case, if *density* is also  
#         ``True``, then the histogram is normalized such that the first bin
#         equals 1.

#     bottom : array-like, scalar, or None, default: None
#         Location of the bottom of each bin, ie. bins are drawn from       
#         ``bottom`` to ``bottom + hist(x, bins)`` If a scalar, the bottom  
#         of each bin is shifted by the same amount. If an array, each bin  
#         is shifted independently and the length of bottom must match the  
#         number of bins. If None, defaults to 0.

#     histtype : {'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'
#         The type of histogram to draw.

#         - 'bar' is a traditional bar-type histogram.  If multiple data    
#           are given the bars are arranged side by side.
#         - 'barstacked' is a bar-type histogram where multiple
#           data are stacked on top of each other.
#         - 'step' generates a lineplot that is by default unfilled.        
#         - 'stepfilled' generates a lineplot that is by default filled.    

#     align : {'left', 'mid', 'right'}, default: 'mid'
#         The horizontal alignment of the histogram bars.

#         - 'left': bars are centered on the left bin edges.
#         - 'mid': bars are centered between the bin edges.
#         - 'right': bars are centered on the right bin edges.

#     orientation : {'vertical', 'horizontal'}, default: 'vertical'
#         If 'horizontal', `~.Axes.barh` will be used for bar-type histograms        and the *bottom* kwarg will be the left edges.

#     rwidth : float or None, default: None
#         The relative width of the bars as a fraction of the bin width.  If
#         ``None``, automatically compute the width.

#         Ignored if *histtype* is 'step' or 'stepfilled'.

#     log : bool, default: False
#         If ``True``, the histogram axis will be set to a log scale.       

#     color : color or array-like of colors or None, default: None
#         Color or sequence of colors, one per dataset.  Default (``None``) 
#         uses the standard line color sequence.

#     label : str or None, default: None
#         String, or sequence of strings to match multiple datasets.  Bar   
#         charts yield multiple patches per dataset, but only the first gets
#         the label, so that `~.Axes.legend` will work as expected.

#     stacked : bool, default: False
#         If ``True``, multiple data are stacked on top of each other If    
#         ``False`` multiple data are arranged side by side if histtype is  
#         'bar' or on top of each other if histtype is 'step'

#     Returns
#     -------
#     n : array or list of arrays
#         The values of the histogram bins. See *density* and *weights* for a        description of the possible semantics.  If input *x* is an array, 
#         then this is an array of length *nbins*. If input is a sequence of
#         arrays ``[data1, data2, ...]``, then this is a list of arrays with
#         the values of the histograms for each of the arrays in the same   
#         order.  The dtype of the array *n* (or of its element arrays) will
#         always be float even if no weighting or normalization is used.    

#     bins : array
#         The edges of the bins. Length nbins + 1 (nbins left edges and right        edge of last bin).  Always a single array even when multiple data 
#         sets are passed in.

#     patches : `.BarContainer` or list of a single `.Polygon` or list of such objects
#         Container of individual artists used to create the histogram      
#         or list of such containers if there are multiple input datasets.  

#     Other Parameters
#     ----------------
#     data : indexable object, optional
#         If given, the following parameters also accept a string ``s``, which is
#         interpreted as ``data[s]`` (unless this raises an exception):     

#         *x*, *weights*

#     **kwargs
#         `~matplotlib.patches.Patch` properties

#     See Also
#     --------
#     hist2d : 2D histogram with rectangular bins
#     hexbin : 2D histogram with hexagonal bins

#     Notes
#     -----
#     For large numbers of bins (>1000), 'step' and 'stepfilled' can be     
#     significantly faster than 'bar' and 'barstacked'.


values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4, 2.6]
plt.hist(values, bins=3, color='purple')
plt.show()

##Example 1 - General histogram
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000001, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388000000000005, 60.916, 70.19800000000001, 82.208, 73.33800000000001, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000001, 71.993, 42.592, 45.678, 73.952, 59.443000000000005, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.906000000000006, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999999, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000001, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.568000000000005, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000001, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]

plt.hist(life_exp, color='limegreen')
plt.show()



##Example 2- Bin size
# #Bin size is very important
# #Too few = oversimplify data
# #Too many = over-complicate data  
#plt.clf() cleans up your plot so you can start again

# Build histogram with 5 bins
plt.hist(life_exp, bins=5, color='red')

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20, color='darkgreen')

# Show and clean up again
plt.show()
plt.clf()


##Example 3 - Compare histograms
#Compare 2 lists, life_exp & life_exp1950

life_exp1950 = [28.8, 55.23, 43.08, 30.02, 62.48, 69.12, 66.8, 50.94, 37.48, 68.0, 38.22, 40.41, 53.82, 47.62, 50.92, 59.6, 31.98, 39.03, 39.42, 38.52, 68.75, 35.46, 38.09, 54.74, 44.0, 50.64, 40.72, 39.14, 42.11, 57.21, 40.48, 61.21, 59.42, 66.87, 70.78, 34.81, 45.93, 48.36, 41.89, 45.26, 34.48, 35.93, 34.08, 66.55, 67.41, 37.0, 30.0, 67.5, 43.15, 65.86, 42.02, 33.61, 32.5, 37.58, 41.91, 60.96, 64.03, 72.49, 37.37, 37.47, 44.87, 45.32, 66.91, 65.39, 65.94, 58.53, 63.03, 43.16, 42.27, 50.06, 47.45, 55.56, 55.93, 42.14, 38.48, 42.72, 36.68, 36.26, 48.46, 33.68, 40.54, 50.99, 50.79, 42.24, 59.16, 42.87, 31.29, 36.32, 41.72, 36.16, 72.13, 69.39, 42.31, 37.44, 36.32, 72.67, 37.58, 43.44, 55.19, 62.65, 43.9, 47.75, 61.31, 59.82, 64.28, 52.72, 61.05, 40.0, 46.47, 39.88, 37.28, 58.0, 30.33, 60.4, 64.36, 65.57, 32.98, 45.01, 64.94, 57.59, 38.64, 41.41, 71.86, 69.62, 45.88, 58.5, 41.22, 50.85, 38.6, 59.1, 44.6, 43.58, 39.98, 69.18, 68.44, 66.07, 55.09, 40.41, 43.16, 32.55, 42.04, 48.45]

#Hist of life_exp w/ 15 bins)
plt.hist(life_exp, bins=15, color='teal')
plt.show()
plt.clf()

#Hist of life_exp1950 w/ 15 bins
plt.hist(life_exp1950, bins=15, color='brown', orientation='horizontal', histtype='step')
plt.show()
plt.clf()

