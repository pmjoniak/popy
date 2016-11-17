from wdi import Array
from duze_cyfry import *
import turtle
import random


def dajCyfreA(n):
	c = dajCyfre(n)
	a = Array(5, 5)
	for x in range(5):
		for y in range(5):
			if c[x][y] == '#':
				a[x][y] = 1
			else:
				a[x][y] = 0
	return a


def kwadrat(bok, kolor):
	turtle.fillcolor(kolor)
	turtle.begin_fill()
	for i in range(4):
		turtle.fd(bok)
		turtle.rt(90)
	turtle.end_fill()


def rysujA(A, bok, kolor):
	for x in range(5):
		for y in range(5):
			if A[x][y] == 1:
				kwadrat(bok, kolor)
			turtle.pu()
			turtle.fd(bok)
			turtle.pd()
		turtle.pu()
		turtle.backward(5 * bok)
		turtle.right(90)
		turtle.forward(bok)
		turtle.left(90)
		turtle.pd()


def wyrysuj(n):
	s = str(n)
	for c in s:
		A = dajCyfreA(c)
		rysujA(A, 10, (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
		turtle.pu()
		turtle.fd(6 * 10)
		turtle.left(90)
		turtle.forward(5 * 10)
		turtle.right(90)
		turtle.pd()


turtle.speed('fastest')
wyrysuj(123456)
turtle.done()
