class Fraction:

	def __init__(self,top,bottom):
		self.num = top
		self.den = bottom

	def __str__(self):
		return (str(self.num) + "/" + str(self.den))

	def show(self):
		print(self.num, "/", self.den)

def main():
	twoFifths = Fraction(2,5)
	print(twoFifths)

main()