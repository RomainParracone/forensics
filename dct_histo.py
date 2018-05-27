# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.fftpack import dct,idct

### First, read the images with mpimg.imread

clean = mpimg.imread('clean.jpeg')
tamper = mpimg.imread('tamper.jpeg')

### Second, convert them to np arrays and compute the gray scale image

clean_gray = np.dot(clean, [0.299, 0.587, 0.144])
tamper_gray = np.dot(tamper, [0.299, 0.587, 0.144])

### Decompose pictures in tiles and print them in a 2D Array 

clean_height, clean_width = clean_gray.shape
tamper_height, tamper_width = tamper_gray.shape
eight = 80
clean_tiles = {}
tamper_tiles ={}

for y in xrange(clean_height):
    for x in xrange(clean_width):
        current_tile = (x/eight, y/eight)
        if not current_tile in clean_tiles:
            clean_tiles[current_tile] = np.zeros((eight,eight))
        clean_tiles[current_tile][(y%eight)][x%eight] = clean_gray[y][x]
        ### Add pixel (y,x) to the right tile mod[eight]

for y in xrange(tamper_height):
    for x in xrange(tamper_width):
        current_tile = (x/eight, y/eight)
        if not current_tile in tamper_tiles:
            tamper_tiles[current_tile] = np.zeros((eight,eight))
        tamper_tiles[current_tile][(y%eight)][x%eight] = tamper_gray[y][x]
 
clean_dct_tiles = {}
tamper_dct_tiles = {}
clean_new_tiles = {}
tamper_new_tiles = {}

### Use this function to store dct coefficients in array

def visualize_dct(d):
    d = d + abs(d.min())
    h = np.histogram(d, bins=1000, range=(0, d.max()))
    c = 255.0*np.cumsum(h[0])/sum(h[0])
    new_img = np.zeros(d.shape)
    for index,value in np.ndenumerate( d ):
        new_img[index] = c[int(999.0*value/d.max())]    
    return new_img  

for key, tile in clean_tiles.iteritems():
    clean_dct_tiles[key] = dct(dct(tile,axis=0), axis=1)
    for y in xrange(eight):
        for x in xrange(eight):
            if x > 60 or y > 60: clean_dct_tiles[key][y][x] = 0
    clean_new_tiles[key] = idct(idct(clean_dct_tiles[key], axis=1), axis=0)/(eight*eight)
    clean_dct_tiles[key] = visualize_dct(clean_dct_tiles[key])

for key, tile in tamper_tiles.iteritems():
    tamper_dct_tiles[key] = dct(dct(tile,axis=0), axis=1)
    for y in xrange(eight):
        for x in xrange(eight):
            if x > 60 or y > 60: tamper_dct_tiles[key][y][x] = 0
    tamper_new_tiles[key] = idct(idct(tamper_dct_tiles[key], axis=1), axis=0)/(eight*eight)
    tamper_dct_tiles[key] = visualize_dct(tamper_dct_tiles[key])


### The following commented lines display one block of real picture and its dct block
"""    
index = (3,4)
plt.imshow(new_tiles[index], cmap = plt.get_cmap('gray'))
plt.show()
plt.imshow(dct_tiles[index], cmap = plt.get_cmap('gray'))
plt.show()
plt.clf()
"""
clean_pixels_wow = np.zeros(clean_gray.shape)
clean_pixels_d = np.zeros(clean_gray.shape)
for y in xrange(clean_height):
    for x in xrange(clean_width):
        current_tile = (x/eight, y/eight)
        clean_pixels_d[y][x] = int(clean_dct_tiles[current_tile][y%eight][x%eight])
        clean_pixels_wow[y][x] = int(clean_new_tiles[current_tile][y%eight][x%eight])
        if x%eight <= 1 or y%eight <= 1: 
            clean_pixels_wow[y][x] = clean_pixels_d[y][x] = 0

plt.imshow(clean_pixels_wow, cmap = plt.get_cmap('gray'))
plt.show()
plt.imshow(clean_pixels_d, cmap = plt.get_cmap('gray'))
plt.savefig('clean_dct')
plt.clf()

tamper_pixels_wow = np.zeros(tamper_gray.shape)
tamper_pixels_d = np.zeros(tamper_gray.shape)
for y in xrange(tamper_height):
    for x in xrange(tamper_width):
        current_tile = (x/eight, y/eight)
        tamper_pixels_d[y][x] = int(tamper_dct_tiles[current_tile][y%eight][x%eight])
        tamper_pixels_wow[y][x] = int(tamper_new_tiles[current_tile][y%eight][x%eight])
        if x%eight <= 1 or y%eight <= 1: 
            tamper_pixels_wow[y][x] = tamper_pixels_d[y][x] = 0

plt.imshow(tamper_pixels_wow, cmap = plt.get_cmap('gray'))
plt.show()
plt.imshow(tamper_pixels_d, cmap = plt.get_cmap('gray'))
plt.savefig('tamper_dct')
plt.clf()
