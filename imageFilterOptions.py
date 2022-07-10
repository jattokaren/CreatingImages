# USAGE EXAMPLES
# python mytestscript.py --image PXL_20210901_192523976.MP_2.jpg
# python mytestscript.py --image PXL_20211128_004326553.jpg
# python mytestscript.py --image IMG_20190621_201755.jpg
# python imageFilterOptions.py --image PXL_20220414_015637240_2.jpg
# python imageFilterOptions.py --image 'PXL_20220430_151124481 (1).jpg'

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import csv
#import exif
import datetime as datetime
import argparse
import cv2
import sys
import matplotlib.pyplot as plt
#from picamera import Color  

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")		# Can have multiple arguments
args = vars(ap.parse_args())

datetimestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#camera.image_effect = effect
#camera.annotate_background = Color('black')
#camera.annotate_text_size = 75
#camera.annotate_text = datetimestamp + '\n' + "Effect: %s" % effect

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

fullfilename = args["image"]
print(fullfilename)
filename = fullfilename[:-4]     # Exclude last 4 characters
print(filename)
filetype = fullfilename[-3:]     # Last 3 characters
print(filetype)
filesize = os.path.getsize(fullfilename)
print(str('File Size: ') + str(filesize))

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))

### Oil Paint Effect
oilpaint50 = cv2.xphoto.oilPainting(image, 50, 1)
#cv2.imwrite("newimage-oilpaint50.jpg", oilpaint50)
cv2.imwrite(str(filename + '-oilpainting_01_50.jpg'), oilpaint50)

oilpaint50 = Image.open(fullfilename)

#title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
title_font = ImageFont.truetype('OpenSans-VariableFont_wdth,wght.ttf', size=2000)

title_text = "The Beauty of Nature"
image_editable = ImageDraw.Draw(oilpaint50)
#image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
image_editable.text((15,15), title_text, (0, 0, 0))
# Starting Coordinates: Pillow library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner.
# Text: String between single or double quotations
# Text color in RGB format: Google Picker is a great resource to find the best color. Search “Color Picker” on Google and it will show up
# Font style: Google Fonts is a great resource to pick your font style, and you can also download the TTF(TrueType Font) file of the font family.
#oilpaint50.save("result.jpg")
oilpaint50.save(str(filename + '-withText.jpg'))

uniqueColors = set()
w, h = oilpaint50.size
for x in range(w):
	for y in range(h):
		pixel = oilpaint50.getpixel((x, y))
		uniqueColors.add(pixel)

totalUniqueColors = len(uniqueColors)
print(totalUniqueColors)

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
cv2.imwrite(str(filename + "-BGR2Gray.jpg"), gray)

blurred = cv2.GaussianBlur(gray, (5,5), 0)
#cv2.imshow("Image Gray Blurred", blurred)
#cv2.waitKey(0)
cv2.imwrite(str(filename + "-BGR2Gray-GaussianBlur.jpg"), blurred)

thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#cv2.imshow("Image Gray Blurred Threshold", thresh)
#cv2.waitKey(0)
cv2.imwrite(str(filename + "-BGR2Gray-GaussianBlur-thresh.jpg"), thresh)


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