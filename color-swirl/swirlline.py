import random

class SwirlLine:
		def __init__(self, xStart, yStart, color, width, height, offset = 0):
			self.xStart = xStart
			self.yStart = yStart
			self.width = width
			self.height = height
			self.color = color
			self.offset = offset
			self.onReset = None
			self.setup()

		def setup(self):
			self.xMin = 0
			self.xMax = self.width-1
			self.yMin = 0
			self.yMax = self.height-1
			self.x = self.xStart
			self.y = self.yStart
			# direction
			self.deltaX = 1
			self.deltaY = 0

		def step(self):
			self.x += self.deltaX
			self.y += self.deltaY

			if self.yMax <= self.yMin and self.xMax <= self.xMin:
				if self.onReset:
					self.onReset()
				self.setup()
				return True

			if self.x > self.xMax and self.deltaX != 0:
				# print("right edge")
				self.yMin += abs(self.deltaX)
				self.x = self.xMax
				self.y = self.yMin
				self.deltaX = 0
				self.deltaY = 1
			if self.y > self.yMax and self.deltaY != 0:
				# print("bottom edge")
				self.xMax -= abs(self.deltaY)
				self.x = self.xMax
				self.y = self.yMax
				self.deltaX = -1
				self.deltaY = 0
			if self.x < self.xMin and self.deltaX != 0:
				# print("left edge")
				self.yMax -= abs(self.deltaX)
				self.x = self.xMin
				self.y = self.yMax
				self.deltaX = 0
				self.deltaY = -1
			if self.y < self.yMin and self.deltaY != 0:
				# print("top edge")
				self.xMin += abs(self.deltaY)
				self.x = self.xMin
				self.y = self.yMin
				self.deltaX = 1
				self.deltaY = 0

		def nextPoint(self):
			point = (self.offset+self.x,self.offset+self.y,self.color)
			didReset = self.step()
			if didReset:
				point = (self.offset+self.x,self.offset+self.y,self.color)
			return point

		# def printLine(self):
			# print("{}x{} - {} \n {} ".format(self.width, self.height, self.numSpots,self.colorGrid))

def main():
	line = SwirlLine(0,0,(0,0,0),3,3)
	for i in range(11):
		print(line.nextPoint())

if __name__ == '__main__':
	main()
