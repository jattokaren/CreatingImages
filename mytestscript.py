# USAGE
# python mytestscript.py --image PXL_20210901_192523976.MP_2.jpg

import os
from datetime import datetime
from PIL import Image
import csv
#import exif
import datetime as datetime
import argparse
import cv2
import sys
import matplotlib.pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

fullfilename = args["image"]
print(fullfilename)
filename = fullfilename[:-4]     # Exclude last 4 characters
print(filename)
filetype = fullfilename[-3:]     # Last 3 characters
print(filetype)
filesize = os.path.getsize(fullfilename)
print(filesize)

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

### Oil Paint Effect
oilpaint50 = cv2.xphoto.oilPainting(image, 50, 1)
#cv2.imwrite("newimage-oilpaint50.jpg", oilpaint50)
cv2.imwrite(str(filename + '-oilpainting_01_50.jpg'), oilpaint50)

oilpaint25 = cv2.xphoto.oilPainting(image, 25, 1)
cv2.imwrite(str(filename + '-oilpainting_02_25.jpg'), oilpaint25)

oilpaint10 = cv2.xphoto.oilPainting(image, 10, 1)
cv2.imwrite(str(filename + '-oilpainting_03_10.jpg'), oilpaint10)

### Heatmap Images
### RGB Image
### Gray Scale
img_RGB_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
filename_RGB_Gray = str(filename + '-RGB-GRAY.jpg')
cv2.imwrite(filename_RGB_Gray, img_RGB_Gray)
### RGB to Gray Scale to Heatmap
img_RGB_Heatmap = cv2.applyColorMap(img_RGB_Gray, cv2.COLORMAP_JET)
filename_RGB_Heatmap = str(filename + '-RGB-Heatmap.jpg')
cv2.imwrite(filename_RGB_Heatmap, img_RGB_Heatmap)

### BGR Image
img_BGR = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
img_BGR_Gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
filename_BGR_Gray = str(filename + '-BGR-GRAY.jpg')
cv2.imwrite(filename_BGR_Gray, img_BGR_Gray)

img_BGR_Heatmap = cv2.applyColorMap(img_BGR_Gray, cv2.COLORMAP_JET)
filename_BGR_Heatmap = str(filename + '-BRG-Heatmap.jpg')
cv2.imwrite(filename_BGR_Heatmap, img_BGR_Heatmap)
#path = 'output'
#cv2.imwrite(os.path.join(path , filename_BGR_Heatmap), img_BGR_Heatmap)


'''
Next Steps
Create an output directory if it is not already there for output images & text files




'''

# show the image and wait for a keypress
#cv2.imshow("Image", image)
#cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
#cv2.imwrite("newimage-ja.jpg", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image Gray", gray)
#cv2.waitKey(0)
cv2.imwrite("newimage-gray.jpg", gray)

blurred = cv2.GaussianBlur(gray, (5,5), 0)
#cv2.imshow("Image Gray Blurred", blurred)
#cv2.waitKey(0)
cv2.imwrite("newimage-blurred.jpg", blurred)

thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#cv2.imshow("Image Gray Blurred Threshold", thresh)
#cv2.waitKey(0)
cv2.imwrite("newimage-blurred-thresh.jpg", thresh)


'''
def main():
	processStartTime = datetime.now()
	print(processStartTime)

	try:
		print("main method starting....")
	except IOError as ioe:
		print("IO Error in Main method")
	finally:
		print("main()  finally block executed")
'''