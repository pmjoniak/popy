import turtle

BOK = 10
kolory = ['red', 'orange', 'green', 'blue']


def prostokat(length):
	turtle.begin_fill()
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(BOK)
	turtle.right(90)
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(BOK)
	turtle.end_fill()
	turtle.right(180)
	turtle.forward(BOK)
	turtle.left(90)


turtle.speed(0)
turtle.tracer(0, 0)


color_num = 0
segments = 50
length = 10
r = (segments * BOK) / (2 * 3.14159265)

for i in range(segments):
	turtle.fillcolor(kolory[color_num])
	color_num = (color_num + 1) % 4
	prostokat(length)
	length = length + 3
	turtle.right(360 / segments)


turtle.setheading(90)
turtle.backward(BOK / 2)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(r + 5)
turtle.end_fill()
turtle.update()
turtle.done()
