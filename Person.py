class Person:
	population = 0

	def __init__(self, name):
		self.name = name
		print("Initializing " + self.name )
		Person.population += 1

	def greet(self):
		print("Hi! My name is ", self.name)

	def howMany(self):
		print(Person.population)

	def leave(self):
		Person.population -= 1
		print(Person.population)


def main():
	barack = Person("Barack")
	barack.greet()
	barack.howMany()

	michelle = Person("Michelle")
	michelle.greet()
	michelle.howMany()
	michelle.leave()



main()