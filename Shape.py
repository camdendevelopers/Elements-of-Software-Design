class Shape:
	description = "These are quadrilaterials"
	author = "Bill Bulko"

	def __init__(self, length, height):
		self.x = length
		self.y = height

	def area(self):
		return (self.x * self.y)

	def perimeter(self):
		return (2 * self.x + 2 * self.y)

class Square(Shape):

	def __init__(self, side):
		self.x = side
		self.y = side




def main():
	myRectangle = Shape(100,50)
	print(myRectangle.author)
	print(myRectangle.area())

	myRectangle2 = Shape(25,80)
	print(myRectangle2.area())
	print(myRectangle2.perimeter())

	mySquare = Square(135)
	print(mySquare.area())


main()