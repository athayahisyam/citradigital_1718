import math, numpy
import scipy.misc
from scipy.misc.pilutil import Image

# membuka gambar
im = Image.open('Fig0316.tif').convert('L')

# gambar di konversi menjadi ndarray

im1 = scipy.misc.fromimage(im)

# mencari nilai minimal dan maksimal dari piksel

b = im1.max()
a = im1.min()

print('minimal value =', a)
print('maximal value =', b)

# converting im1 to float

c = im1.astype(float)

# contrast stretching transformation

im2 = 255*(c-a)/(b-a)

#im2 is converted from ndarray to an image

im3 = scipy.misc.toimage(im2)

# saving im3 as contrast_output.png in tgs_uts folder

im3.save('contrast_output3.png')
