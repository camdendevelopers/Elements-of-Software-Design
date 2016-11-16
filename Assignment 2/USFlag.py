#  File: USFlag.py
#  Description: Program that prompts user for a desired flag height and the U.S flag is drawn with accurate proportion
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: September 11, 2016
#  Date Last Modified: September 16, 2016


import turtle
import math

V_PADDING = 100
H_PADDING = 100

def drawStar(ttl, k, x, y):
	#ttl.goto(x, y)
	ttl.penup()
	r = k / 2
	a = (r / math.sin(math.radians(126))) * math.sin(math.radians(18))
	side = math.sqrt(r**2 + a**2 - 2 * a * r * math.cos(math.radians(36)))
	xStar = a * math.cos(math.radians(56))
	yStar = a * math.sin(math.radians(56))
	#angle = 140
	angle = 142

	ttl.goto((-xStar)+x,y + yStar)
	ttl.fillcolor("white")
	ttl.begin_fill()
	ttl.pendown()
	for i in range(5):
		ttl.forward(side)
		ttl.right(angle)
		ttl.forward(side)
		ttl.right(72 - angle)
	ttl.end_fill()

def drawStars(ttl, x_origin, y_origin,c, d, k, g, e): 
	ox = x_origin
	oy = y_origin
	x_origin = int(x_origin)
	y_origin = int(y_origin)
	c = int(c)
	d = int(d)
	e = int(e)
	g = int(g)
	HEIGHT = int(9 * e)
	WIDTH = int(11 * g)


	ttl.penup()
	ttl.right(180)
	ttl.speed(0)
	ttl.pendown()
	for i in range(y_origin, y_origin - c + e, -(2*e)):
		for j in range(x_origin, x_origin + d - g, (2*g)):
			drawStar(ttl, k, j, i)


	for i in range(y_origin - e, y_origin - c + (2 * e), -(2*e)):
		for j in range(x_origin + g, x_origin + d - (2* g), (2*g)):
			drawStar(ttl, k, j, i)
	
def drawCanton(ttl, a, b, c, d):
	ttl.fillcolor("#002868") #Glory Blue
	ttl.penup() 
	ttl.goto(-(b / 2), (a / 2)) 
	ttl.pendown() 
	ttl.begin_fill() 
	ttl.left(90)
	ttl.forward(c)
	ttl.left(90)
	ttl.forward(d)
	ttl.left(90)
	ttl.forward(c)
	ttl.left(90)
	ttl.forward(d) 
	ttl.end_fill()

def drawStripes(ttl, x_origin, y_origin, l, b):
	ttl.fillcolor("#BF0A30") #Glory Red
	ttl.penup() 
	ttl.goto(x_origin, y_origin) 
	ttl.speed(0)
	for i in range(8):
		ttl.pendown() 
		ttl.begin_fill()
		ttl.left(90)
		ttl.forward(l)
		ttl.left(90)
		ttl.forward(b)
		ttl.left(90)
		ttl.forward(l)
		ttl.left(90)
		ttl.forward(b)
		ttl.penup()
		ttl.goto(x_origin, y_origin - (2 * l * i))
		ttl.end_fill()
	ttl.speed(2)

def drawFlag(ttl, a, b):
	#Define all variables and measurements	
	c = a * (7/13)
	d = b * (2/5)
	e = c / 10
	f = e
	g = d / 12
	h = g
	l = a / 13
	k = l * (4/5)
	x_origin = -(b / 2)
	y_origin = a / 2

	#Draw flag outline
	ttl.penup() 
	ttl.goto(x_origin, y_origin) 
	ttl.pendown() 
	ttl.right(90)
	ttl.forward(a)
	ttl.left(90)
	ttl.forward(b)
	ttl.left(90)
	ttl.forward(a)
	ttl.left(90)
	ttl.forward(b)

	#Draw stripes
	drawStripes(ttl, x_origin, y_origin, l, b)
	
	#Draw canton
	drawCanton(ttl, a, b, c, d)

	#Draw stars
	drawStars(ttl, x_origin + g, y_origin - e, c, d, k, g, e)

def main():
	#Define turtle variables
	ttl = turtle.Turtle()
	screen = turtle.Screen()
	screen.title ("United States Flag Creator")

	#Prompt user for input
	a = round(eval(turtle.textinput("","Please enter a desired flag height: ")))
	b = a * 1.9

	#Setup screen size based on height given
	screen.setup((2 * H_PADDING + b),(2 * V_PADDING + a),0,0)

	#Draw Flag
	drawFlag(ttl, a, b)

	#End turtle when user clicks screen
	turtle.exitonclick()

main()
