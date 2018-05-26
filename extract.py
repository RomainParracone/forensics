#!/usr/bin/python3

import PIL.Image
import sys

filename = sys.argv[1]
img= PIL.Image.open(filename)

exif_data = img._getexif()

print(exif_data)
