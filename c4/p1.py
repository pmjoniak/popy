import turtle
import random
from PIL import Image


def kwadrat(bok, kolor):
	# turtle.pencolor(kolor)
	turtle.fillcolor(kolor)
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(bok)
		turtle.left(90)
	turtle.end_fill()


def kwadrat2(n, img, bok=10):
	resized = img.resize((n, n))
	for i in range(n):
		for j in range(n):
			# kolor = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
			k = resized.getpixel((i, j))
			# print(k)
			if k[3] == 0:
				kolor = (1, 1, 1)
			else:
				kolor = (k[0] / 255, k[1] / 255, k[2] / 255)
			kwadrat(bok, kolor)
			turtle.forward(bok)
		turtle.left(90)
		turtle.forward(bok)
		turtle.left(90)
		turtle.forward(bok * n)
		turtle.left(180)


im = Image.open("python.png")
im = im.rotate(-90)

turtle.speed(0)
turtle.tracer(0, 0)
for i in range(10000):
	im = im.rotate(2)
	turtle.pu()
	turtle.goto(-200, -200)
	turtle.pd()
	kwadrat2(40, im, 10)
	turtle.update()
turtle.done()
