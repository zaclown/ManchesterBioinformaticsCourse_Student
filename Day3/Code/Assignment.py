#!/home/giovanni/code/bioinformatics-course/bin/python3

"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional
"""

# Chinna and Giovanni, 18/01/2022

# before launching this script, make sure to activate the proper environment:

# $ source /home/giovanni/code/bioinformatics-course/bin/activate
# or conda activate
#
#then 
#
# $ cd ManchesterBioinformaticsCourse_Student/Day3/Code

# import the required modules

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize


# load the file lungs.jpg and display it

im = io.imread("/home/giovanni/code/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg", as_gray=True)
plt.imshow(im)
plt.show()

print(im.shape)    # im is an array with 569 rows and 600 columns

# in order to plot the values, the array needs to be flatten
flatim= im.flatten()
# flatim is a one-dimensional array containing 341400 (569 * 600) elements
print(flatim.shape)   

# Plot a histogram of the image

fig = plt.figure()

ax = fig.add_subplot(311)         # set the stage for a figure with 3 rows and 1 column
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
ax.imshow(im, interpolation="none", cmap="Greys_r")
ax2.hist(flatim, bins=599, facecolor="c", edgecolor= "c")
ax3.hist(flatim, bins=599, facecolor="c", edgecolor= "c")
# for an easier reading of the distribution of values > 0, change the y axis scale
ax3.set_ylim(ymin=0, ymax=2000)                             

plt.show()

# Write a function that displays the CT image with different window levels. The input variables
# should be the window and the level.
# the Hounsfield units that make up the grayscale in medical CT imaging have a scale from black to
# white of 4096 values (12 bit), from -1024 HU to 3071 HU. By expressing window and levels as fractions
# of 4096, they can be mapped to 0-1 scale of the gray levels in the .png image 

def imagelevels(window, level):
    im = io.imread("/home/giovanni/code/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg", as_gray=True)
    #flatim= im.flatten()
    windowst= int(window)/4096
    levelst= int(level)/4096
    vis_min = levelst - windowst/2
    vis_max = levelst + windowst/2
    plt.imshow(im, cmap='Greys_r', vmin=vis_min, vmax=vis_max)
    plt.show()

imagelevels(900, 1740)  # these values try to capture the central peak of the spctrum
imagelevels(200, 950)   # these values try to capture the first peak of the spctrum (roughly soft tisues)
imagelevels(200, 2600)  











