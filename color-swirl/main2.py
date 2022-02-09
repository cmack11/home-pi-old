import time
import sys

from colorgrid import ColorGrid
from swirlline import SwirlLine
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
class SwirlAnimationOptions:
	self.options = RGBMatrixOptions()
	self.options.rows = 32
	self.options.cols = 32
	self.options.chain_length = 1
	self.options.parallel = 1
	self.options.hardware_mapping = 'adafruit-hat'

	self.matrix = RGBMatrix(options = options)

	self.numSpots = 0
	self.maxSpots = (32*32) // 4

	self.colorGrid = ColorGrid(32,32,numSpots)
	self.swirlLine = SwirlLine(0,0, (255,255,255), 32,32)

	def onSwirlLineReset(self):
		self.matrix.Clear()
		self.numSpots += 1
		self.numSpots %= maxSpots
		self.colorGrid = ColorGrid(32,32,numSpots)
		for point in self.colorGrid.getPoints():
			self.matrix.SetPixel(point['x'],point['y'],point['color']['r'],point['color']['g'],point['color']['b'])

def main():
	swirlAnimationOptions = SwilrAnimationOptions()
	swirlLine.onReset = swirlAnimationOptions.onSwirlLineReset
	for point in colorGrid.getPoints():
		matrix.SetPixel(point['x'],point['y'],point['color']['r'],point['color']['g'],point['color']['b'])

	try:
		print("Press CTRL-C to stop.")
		while True:
			point = swirlLine.nextPoint()
			x = point[0]
			y = point[1]
			color = point[2]
			if colorGrid.getPoint(x,y) != None:
				newColor = colorGrid.getPoint(x,y)
				color = (newColor['r'], newColor['g'], newColor['b'])
				swirlLine.color = color
			matrix.SetPixel(x, y, color[0], color[1], color[2])

			time.sleep(.01)

	except KeyboardInterrupt:
		sys.exit(0)


if __name__ == '__main__':
	main()
