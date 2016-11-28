import turtle


def kwadrat(bok, kolor):
	# turtle.pencolor(kolor)
	turtle.fillcolor(kolor)
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(bok)
		turtle.left(90)
	turtle.end_fill()


def kwadrat2(img, bok=10):
	for i in range(len(img)):
		for j in range(len(img[i])):
			k = img[i][j]
			kolor = (k[0] / 255, k[1] / 255, k[2] / 255)
			kwadrat(bok, kolor)
			turtle.forward(bok)
		turtle.update()
		turtle.left(90)
		turtle.forward(bok)
		turtle.left(90)
		turtle.forward(bok * len(img[i]))
		turtle.left(180)


colors = []
for wiersz in open('krowileb.txt'):
	row = []
	wiersz = wiersz[:-1]
	rgbs = wiersz.split(" ")
	for rgb in rgbs:
		row.append(eval(rgb))
	colors.append(row)

turtle.tracer(0, 0)
turtle.pu()
turtle.goto(-200, -300)
turtle.pd()
kwadrat2(colors, 10)
turtle.update()
turtle.done()
