import turtle
import random


def snieg(n):
	angle = 360 / n
	for i in range(n):
		turtle.forward(100)
		for j in range(n):
			turtle.forward(10)
			turtle.backward(10)
			turtle.left(angle)
		turtle.backward(100)
		turtle.left(angle)


lens = [1, 2, 5, 10, 20, 50, 100]


def drzewo(pos, heading, n):
	if n < 7:
		return

	ratio = 0.8
	turtle.pu()
	turtle.setpos(pos)
	turtle.setheading(heading)
	turtle.pd()
	turtle.forward(n)

	angle = random.randrange(15, 25)
	pos = turtle.pos()
	heading = turtle.heading()
	drzewo(pos, heading + angle, n * ratio)
	drzewo(pos, heading - angle, n * ratio)


def linia(d, n):
	if n == 0:
		turtle.forward(d)
	else:
		linia(d / 3, n - 1)
		turtle.left(90)
		linia(d / 4, n - 1)
		turtle.right(90)
		linia(d / 3, n - 1)
		turtle.right(90)
		linia(d / 4, n - 1)
		turtle.left(90)
		linia(d / 3, n - 1)


def fraktal(d, n):
	turtle.pu()
	turtle.backward(d / 2)
	turtle.left(90)
	turtle.forward(d / 2)
	turtle.right(90)
	turtle.pd()
	linia(d, n)
	turtle.right(90)
	linia(d, n)
	turtle.right(90)
	linia(d, n)
	turtle.right(90)
	linia(d, n)

def dywan(pos, length, d):
	if d == 0:
		return
	turtle.pu()
	turtle.setpos(pos)
	turtle.setheading(0)
	turtle.pd()
	turtle.forward(length)
	turtle.left(90)
	turtle.forward(length)
	turtle.left(90)
	turtle.forward(length)
	turtle.left(90)
	turtle.forward(length)
	dywan(pos + turtle.Vec2D(-2 * length / 3, length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(4 * length / 3, length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(length / 3, -2 * length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(length / 3, 4 * length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(-2 * length / 3, 4 * length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(-2 * length / 3, -2 * length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(4 * length / 3, 4 * length / 3), length / 3, d - 1)
	dywan(pos + turtle.Vec2D(4 * length / 3, -2 * length / 3), length / 3, d - 1)


turtle.speed(0)
#turtle.tracer(10000, 0)
dywan(turtle.Vec2D(-100, 0), 200, 6)
#snieg(20)
#drzewo(turtle.pos(), 90, 50)
#fraktal(200, 4)
turtle.done()
