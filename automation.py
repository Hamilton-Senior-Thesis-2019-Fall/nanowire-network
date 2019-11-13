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

# TODO:
# INTEGRATE WITH BETTER PREPROCESSING
# FIX ISSUE WITH THE FILLED IN NODES BEING JUST ONE
# Fix issue when it identifies letters on bottom as nodes

# CALL THIS FROM LOGIC TO GET SLICES OF LOCATIONS
def findNodes(filename):
    # filename = '040519_P9_009_cropped.tif'
    # filename2 = '040519_E5_013.tif'

    image = plt.imread(filename)
    cells = np.asarray(image)

    scalebar_start = np.size(cells, 0)
    found_scalebar = False
    for row in range(np.size(cells, 0)):
        if not found_scalebar:
            if np.amin(cells[row]) == 0:
                scalebar_start = row
                found_scalebar = True

    cells = cells[:scalebar_start][:]

    rgb_arr = np.stack((cells, cells, cells), axis=-1)

    greyscale = color.rgb2gray(cells)
    gray = exposure.rescale_intensity(greyscale)
    im_thresh = filters.threshold_minimum(gray)


    # print(binary)

    cells = filters.rank.median(gray, morphology.disk(7))

    binary = cells > im_thresh * .6
    for i in range(5):
        binary = morphology.erosion(binary)

    binary = morphology.remove_small_objects(binary, min_size=64)
    binary = 1 - binary
    #plt.imshow(binary)
    #plt.show()

    #
    # plt.imshow(binary_denoise, cmap='Greys',  interpolation='nearest')
    #plt.imshow(cells, cmap='Greys',  interpolation='nearest')
    #plt.show()

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

    elevation_map = filters.sobel(cells)

    #markers = np.zeros_like(cells)
    #markers[cells < 50] = 1
    #markers[cells > 120] = 2

    markers = filters.rank.gradient(cells, morphology.disk(6), mask=binary) < 20
    markers = ndi.label(markers)[0]



    #gradient = filters.rank.gradient(cells, morphology.disk(2))



    segmentation = morphology.watershed(elevation_map, markers, compactness=100, mask=binary)

    # NEXT LINE IS ISSUE IF THERE IS A BUNCH OF CELLS BUT NECESSARY FOR
    # THE PROGRAM TO RECOGNIZE DIFFERENT CELLS- NOT SURE WHY
    segmentation = ndi.binary_fill_holes(segmentation - 1)
    labeled_cells, cell_num = ndi.label(segmentation)
    sizes = np.bincount(labeled_cells.ravel())
    for x, size in enumerate(sizes):
        if (size < 900):
            np.delete(sizes, [x])
    # print(sizes)
    # print(sizes.mean())
    # print(np.median(sizes))
    cellLocs = ndi.find_objects(labeled_cells)
    return [cellLocs, sizes.mean() + np.median(sizes) /2]
    # print('Cells', cells)
    # print('Markers', markers)
    # print('LABEL', labeled_cells)
    # # print('\n'.join([''.join(['{:4}'.format(('', item) [item != 0]) for item in row])
    # #       for row in labeled_cells]))
    # print('Cell Number:', cell_num)
    # print('object locations:', cellLocals)
    # io.imshow(elevation_map)
    # io.imshow(segmentation)
    # io.imshow(labeled_cells)
    # io.show()
#
#
# filename = '040519_P9_009_cropped.tif'
# # filename2 = '040519_E5_013.tif'
#
# image = plt.imread(filename)
# cells = np.asarray(image)
# # rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)
# #
# # greyscale = color.rgb2gray(rgb_arr)
# # gray = exposure.rescale_intensity(greyscale)
# # im_thresh = filters.threshold_minimum(greyscale)
# # binary = greyscale < im_thresh * .7
# # binary_denoise = filters.rank.median(binary, morphology.disk(5))
# #
# # plt.imshow(binary_denoise, cmap='Greys',  interpolation='nearest')
# # plt.show()
#
#
# # edges = feature.canny(gray/255.)
# # # edges = filters.sobel(gray)
# # fill_cells = ndi.binary_fill_holes(edges)
# # label_objects, nb_labels = ndi.label(fill_cells)
# # sizes = np.bincount(label_objects.ravel())
# # mask_sizes = sizes > 20
# # mask_sizes[0] = 0
# # cells_cleaned = mask_sizes[label_objects]
#
# # Trying to get labels to change to individual cells
# # then can use that with find objects
# elevation_map = filters.sobel(cells)
#
# markers = np.zeros_like(cells)
# markers[cells < 50] = 1
# markers[cells > 120] = 2
#
# segmentation = morphology.watershed(elevation_map, markers)
# segmentation = ndi.binary_fill_holes(segmentation - 1)
# labeled_cells, cell_num = ndi.label(segmentation)
# cellLocs = ndi.find_objects(labeled_cells)
# # print('Cells', cells)
# # print('Markers', markers)
# # print('LABEL', labeled_cells)
# # # print('\n'.join([''.join(['{:4}'.format(('', item) [item != 0]) for item in row])
# # #       for row in labeled_cells]))
# # print('Cell Number:', cell_num)
# # print('object locations:', cellLocals)
# # io.imshow(elevation_map)
# io.imshow(segmentation)
# # io.imshow(labeled_cells)
# io.show()
