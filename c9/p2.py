import turtle
import math


def drzewo(a, angle, deep):
	if deep == 0:
		return
	angle_rad = math.radians(angle)
	c = a * math.cos(angle_rad)
	b = a * math.sin(angle_rad)
	for i in range(4):
		turtle.forward(a)
		turtle.right(90)
	turtle.forward(a)
	head, pos = turtle.heading(), turtle.pos()
	turtle.left(angle)
	drzewo(c, angle, deep - 1)
	turtle.pu()
	turtle.setpos(pos)
	turtle.setheading(head)
	turtle.right(90 - angle)
	turtle.forward(c)
	turtle.pd()
	drzewo(b, angle, deep - 1)


turtle.tracer(0, 0)
turtle.left(90)
turtle.color('green')
drzewo(100, 39, 15)
turtle.update()
turtle.done()
