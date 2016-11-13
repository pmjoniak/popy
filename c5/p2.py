import turtle
import random
import math


def mieszaj(k1, k2, a):
	return (k1[0] * a + k2[0] * (1 - a), k1[1] * a + k2[1] * (1 - a), k1[2] * a + k2[2] * (1 - a))


def kwadra(x, y, size, k):
	turtle.pu()
	turtle.goto(x, y)
	turtle.pd()
	turtle.fillcolor(k)
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(size)
		turtle.right(90)
	turtle.end_fill()


k1 = (1, 0, 0)
k2 = (0, 0, 1)
k3 = (1, 0, 1)
k4 = (0, 1, 0)


def migacze(X, Y):
	x = random.randrange(X)
	y = random.randrange(Y)
	size = random.randrange(5, 20)
	a = (1 + math.sin(4 * 3.141592 * (x / X))) / 2
	b = (1 + math.sin(8 * 3.141592 * (y / Y))) / 2
	ka = mieszaj(k1, k2, a)
	kb = mieszaj(k3, k4, b)
	k = mieszaj(ka, kb, 0.5)
	kwadra(x, y, size, k)
	turtle.update()


turtle.tracer(0, 0)

while True:
	migacze(300, 300)

turtle.done()




