import random

class Color:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

def randomColor():
	return {
		'r': random.randint(0,255),
		'g': random.randint(0,255),
		'b': random.randint(0,255),
	}

class ColorGrid:
		def __init__(self, *args):
			self.width = max(args[0], 2)
			self.height = max(args[1], 2)
			self.totalSpots = self.width * self.height
			if len(args) > 2:
				self.numSpots = args[2]
			else:
				self.numSpots = random.randint(1,self.totalSpots // 5)
			self.numSpots = min(self.numSpots, self.totalSpots)
			self.colorGrid  = [[None for x in range(self.width)] for y in range(self.height)]
			randomGrid = [[{'x':x,'y':y} for x in range(self.width)] for y in range(self.height)]
			spotsLeft = self.numSpots
			while spotsLeft > 0:
				row = random.randint(0, len(randomGrid)-1)
				col = random.randint(0, len(randomGrid[row])-1)
				point = randomGrid[row][col]
				self.colorGrid[point['x']][point['y']] = randomColor()
				del randomGrid[row][col]
				if len(randomGrid[row]) < 1:
					del randomGrid[row]

				spotsLeft -= 1

		def getPoint(self, x, y):
			color = self.colorGrid[x][y]
			if color == None:
				return None
			else:
				return {'x':x, 'y':y, 'r':color['r'], 'g':color['g'], 'b':color['b']}

		def getPoints(self):
			arr = []
			for i in range(0, len(self.colorGrid)):
				for j in range(0, len(self.colorGrid[i])):
					if self.colorGrid[i][j] != None:
						arr.append({'x':i, 'y':j, 'color': self.colorGrid[i][j]})
			return arr

		def printGrid(self):
			print("{}x{} - {} \n {} ".format(self.width, self.height, self.numSpots,self.colorGrid))


def main():
	grid = ColorGrid(5,5)
	grid.printGrid()
	print(grid.getPoint(1,1))

if __name__ == '__main__':
	main()
