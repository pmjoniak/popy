import turtle
import math


def mieszanina(k1, k2, a):
	# r1,g1,b1 = k1
	r1 = k1[0]
	g1 = k1[1]
	b1 = k1[2]
	r2, g2, b2 = k2
	r3 = (1 - a) * r1 + a * r2
	g3 = (1 - a) * g1 + a * g2
	b3 = (1 - a) * b1 + a * b2
	return (r3, g3, b3)


def drzewo(a, angle, deep, choinka):
	if deep == 0:
		return
	angle_rad = math.radians(angle)
	c = a * math.cos(angle_rad)
	b = a * math.sin(angle_rad)

	kolor = mieszanina((0, 1, 0), (0.5, 0.2, 0.2), math.pow(deep / MAX_DEEP, 0.3))
	turtle.fillcolor(kolor)
	turtle.color(kolor)
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(a)
		turtle.right(90)
	turtle.end_fill()
	turtle.forward(a)
	head, pos = turtle.heading(), turtle.pos()

	turtle.begin_fill()
	turtle.right(90 - angle)
	turtle.forward(c)
	turtle.right(90)
	turtle.forward(b)
	turtle.right(90 + angle)
	turtle.forward(a)
	turtle.right(90)
	turtle.end_fill()


	turtle.left(angle)
	if choinka:
		drzewo(c, 90 - angle, deep - 1, choinka)
	else:
		drzewo(c, angle, deep - 1, choinka)
	turtle.pu()
	turtle.setpos(pos)
	turtle.setheading(head)
	turtle.right(90 - angle)
	turtle.forward(c)
	turtle.pd()
	if choinka:
		drzewo(b, 90 - angle, deep - 1, choinka)
	else:
		drzewo(b, angle, deep - 1, choinka)


turtle.tracer(100, 0)
turtle.left(90)
turtle.pu()
turtle.setpos(-200, -200)
turtle.pd()
MAX_DEEP = 12
# drzewo(60, 35, MAX_DEEP, True)
drzewo(100, 39, MAX_DEEP, False)
turtle.update()
turtle.done()
