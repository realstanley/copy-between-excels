#!/usr/bin/env python
# coding=utf-8

import Image
import sys
if (len(sys.argv) != 3):
	print "Usage:" + sys.argv[0] + "<src> <dst>"
	exit()
img = Image.open(sys.argv[1])
img.save(sys.argv[2])
