import matplotlib.pyplot as plt
import numpy as np
import math
from skimage import io
from skimage import feature
from skimage import draw
from skimage import util
from skimage import color
from skimage import morphology
from skimage import filters
from skimage import measure
from skimage import transform
from skimage import exposure
from skimage import segmentation as segs
from scipy import ndimage as ndi
from sklearn.neighbors import NearestNeighbors
import matplotlib.lines as lines
import os
filename = '040519_P9_009_cropped.tif'
# filename2 = '040519_E5_013.tif'

image = plt.imread(filename)
cells = np.asarray(image)
# rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)
#
# greyscale = color.rgb2gray(rgb_arr)
# gray = exposure.rescale_intensity(greyscale)
# im_thresh = filters.threshold_minimum(greyscale)
# binary = greyscale < im_thresh * .7
# binary_denoise = filters.rank.median(binary, morphology.disk(5))
#
# plt.imshow(binary_denoise, cmap='Greys',  interpolation='nearest')
# plt.show()


# edges = feature.canny(gray/255.)
# # edges = filters.sobel(gray)
# fill_cells = ndi.binary_fill_holes(edges)
# label_objects, nb_labels = ndi.label(fill_cells)
# sizes = np.bincount(label_objects.ravel())
# mask_sizes = sizes > 20
# mask_sizes[0] = 0
# cells_cleaned = mask_sizes[label_objects]

# Trying to get labels to change to individual cells
# then can use that with find objects

markers = np.zeros_like(cells)
markers[cells < 55] = 1
markers[cells > 120] = 2
elevation_map = filters.sobel(cells)
segmentation = morphology.watershed(elevation_map, markers)
labeled_cells, cell_num = ndi.label(segmentation)
print('Cells', cells)
print('Markers', markers)
print('LABEL', labeled_cells)
print('Cell Number:', cell_num)
# io.imshow(elevation_map)
io.imshow(segmentation)
io.imshow(labeled_cells)
io.show()
