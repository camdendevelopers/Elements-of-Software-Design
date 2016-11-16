def updateVars(a,b):
	a = 5
	b[2] = "new two"
	print(a)
	print(b)
	return (a,b)





#x = 10
#y = ["zero"...."three"]

#Call by value language: Main passes a copy of variables that will not affect original
#Call by reference language: Passes memory pointer of variables to function and will affect all variables

#Python uses call by object: 
def main():

	x = 10
	y = ["zero", "one", "two","three"]

	print(updateVars(x,y))

main()
