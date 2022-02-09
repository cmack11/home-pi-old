#!/usr/bin/env python
import time
import sys

from colorgrid import ColorGrid
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

time.sleep(5)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)
canvas = matrix

numSpots = 0
maxSpots = (32*32) // 4
colorGrid = ColorGrid(32,32,numSpots)
r = 255
g = 255
b = 255

x = 0
deltaX = 1
y = 0
deltaY = 0
xMin = 0
xMax = 31
yMin = 0
yMax = 31

offset_canvas = matrix.CreateFrameCanvas()

for point in colorGrid.getPoints():
	matrix.SetPixel(point['x'],point['y'],point['color']['r'],point['color']['g'],point['color']['b'])

try:
	print("Press CTRL-C to stop.")
	while True:
		if yMax <= yMin and xMax <= xMin:
			matrix.Clear()
			x = 0
			y = 0
			deltaX = 1
			deltaY = 0
			xMin = 0
			xMax = 31
			yMin = 0
			yMax = 31
			numSpots += 1
			numSpots %= maxSpots
			colorGrid = ColorGrid(32,32,numSpots)
			for point in colorGrid.getPoints():
			        matrix.SetPixel(point['x'],point['y'],point['color']['r'],point['color']['g'],point['color']['b'])

			continue
		if colorGrid.getPoint(x,y) != None:
			r = colorGrid.getPoint(x,y)['r']
			b = colorGrid.getPoint(x,y)['b']
			g = colorGrid.getPoint(x,y)['g']

		matrix.SetPixel(x,y, r, g, b)

		x += deltaX
		y += deltaY

		if x > xMax and deltaX != 0:
			# print("right edge")
			yMin += abs(deltaX)
			x = xMax
			y = yMin
			deltaX = 0
			deltaY = 1
		if y > yMax and deltaY != 0:
			# print("bottom edge")
			xMax -= abs(deltaY)
			x = xMax
			y = yMax
			deltaX = -1
			deltaY = 0
		if x < xMin and deltaX != 0:
			# print("left edge")
			yMax -= abs(deltaX)
			x = xMin
			y = yMax
			deltaX = 0
			deltaY = -1
		if y < yMin and deltaY != 0:
			# print("top edge")
			xMin += abs(deltaY)
			x = xMin
			y = yMin
			deltaX = 1
			deltaY = 0
		# offset_canvas = matrix.SwapOnVSync(offset_canvas)
		time.sleep(.001)

		# print("x: {} y: {} {}:{}|{}:{}".format(x, y, xMin, xMax, yMin, yMax))
except KeyboardInterrupt:
	sys.exit(0)
