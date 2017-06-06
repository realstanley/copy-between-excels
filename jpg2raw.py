import Image
import sys
import struct

if (len(sys.argv) != 3):
	raise Exception("Usage: %s <input_image> <output_dump>" % sys.argv[0])

im = Image.open(sys.argv[1])
outf = open(sys.argv[2],"wb")

print "Image size: %dx%d" % im.size

data = im.getdata()

for (r,g,b) in data:
	outf.write(struct.pack('BBB',r,g,b))

outf.close()
