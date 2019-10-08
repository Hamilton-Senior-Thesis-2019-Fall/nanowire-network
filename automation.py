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
from sklearn.neighbors import NearestNeighbors
import matplotlib.lines as lines
import os

filename = '040519_P9_009_cropped.tif'

image = plt.imread(filename)
gray_arr = np.asarray(image)
rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)

greyscale = color.rgb2gray(rgb_arr)
im_thresh = filters.threshold_minimum(greyscale)
binary = greyscale < im_thresh * 0.75
binary_denoise = filters.rank.median(binary, morphology.disk(5))

plt.imshow(binary_denoise, cmap='Greys',  interpolation='nearest')
plt.show()
