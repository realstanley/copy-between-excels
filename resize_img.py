#!/usr/bin/env python
# coding=utf-8

import Image
import sys
import struct
if(len(sys.argv) != 3):
	print "Usage:" + sys.argv[0] + "<width> <height>"
	exit()

width = int(sys.argv[1])
height = int(sys.argv[2])
print "width * height :" +  str(width) + '*' + str(height)

img = Image.open("cat_299x299.jpg")
img.resize((width, height), Image.ANTIALIAS).save("cat_%dx%d.jpg" %(width, height))
