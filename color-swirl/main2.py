import time
import sys

from colorgrid import ColorGrid
from swirlline import SwirlLine
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

def main():
	options = RGBMatrixOptions()
	options.rows = 32
	options.cols = 32
	options.chain_length = 1
	options.parallel = 1
	options.hardware_mapping = 'adafruit-hat'

	matrix = RGBMatrix(options = options)

	numSpots = 0
	maxSpots = (32*32) // 4

	colorGrid = ColorGrid(32,32,numSpots)
	swirlLine = SwirlLine(0,0, (255,255,255), 32,32)

	for point in colorGrid.getPoints():
		matrix.SetPixel(point['x'],point['y'],point['color']['r'],point['color']['g'],point['color']['b'])

	try:
		print("Press CTRL-C to stop.")
		while True:
			point = swirlLine.nextPoint()

			print(point)
			time.sleep(.1)

	except KeyboardInterrupt:
		sys.exit(0)


if __name__ == '__main__':
	main()
