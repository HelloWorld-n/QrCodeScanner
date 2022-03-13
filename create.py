#!/bin/python3
import qrcode
import datetime
import colorsys 
 
def bytenumToHexstr(bytenum):
	hexstr = hex(bytenum)[2:]
	if len(hexstr) < 2:
		hexstr = "0" + hexstr.upper()
	return hexstr

def colorToColorStr(color):
	red, green, blue = color["red"], color["green"], color["blue"]
	return "#" + bytenumToHexstr(red) + bytenumToHexstr(green) + bytenumToHexstr(blue) 
 
def getDistinctColorPair(): 
	import random
	while True:
		colors = [
			{"red": random.randint(0, 255), "green": random.randint(0, 255), "blue": random.randint(0, 255)} for i in range(0, 2)
		]
		sumsOfSpecColors = [0, 0]
		for specColor in ["red", "green", "blue"]:
			sumsOfSpecColors[0] += colors[0][specColor]
			sumsOfSpecColors[1] += colors[1][specColor]
		
		if abs(sumsOfSpecColors[0] - sumsOfSpecColors[1]) < 128:
				continue
		
		colors = [colorToColorStr(color) for color in colors]
		return colors

distinctColorPair = getDistinctColorPair()

qr = qrcode.QRCode()

qr.add_data(str(datetime.datetime.utcnow()).replace(" ", " t ") + " (UTC)")

img = qr.make_image(back_color=distinctColorPair[0], fill_color=distinctColorPair[1])
img.save(".img.png")

