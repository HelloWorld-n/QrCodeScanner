#!/bin/python3
import cv2
import webbrowser

def scanQr(inv = False):
	img = cv2.imread(".img.png")
	if inv:
		img = cv2.bitwise_not(img)
	det = cv2.QRCodeDetector()
	return det.detectAndDecode(img)

val, pts, st_code = scanQr()

if val == "":
	val, pts, st_code = scanQr(inv = True)

if val == "":
	print("System failed to load qrCode! ")
else:
	print(val)
