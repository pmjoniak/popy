from turtle import *

speed('fastest')

BOK = 20


def kwadrat(bok, kolor):
	fillcolor(kolor)
	begin_fill()
	for i in range(4):
		fd(bok)
		rt(90)
	end_fill()


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


def zlicz(znak, napis):
	licznik = 0
	for z in napis:
		if z == znak:
			licznik += 1
	return licznik


def murek(prog, kolory):
	kolor = kolory[0]
	# N = zlicz('f', prog)
	pozycja = 0
	for x in prog:
		if x == 'f':
			# a = pozycja / N
			kwadrat(BOK, kolor)
			pozycja += 1
			fd(BOK)
		elif x == 'r':
			rt(90)
			fd(BOK)
		elif x == 'l':
			bk(BOK)
			lt(90)
		elif x == 'u':
			print('pu')
			pu()
		elif x == 'd':
			pd()
		elif x in '0123456789':
			kolor = kolory[int(x)]

s = 4 * ('0' + 5 * 'f' + '1' + 5 * 'f' + 'u' + 10 * 'b' + 'r' + 'd')
print(s)
murek(s , [(0.5, 1, 0), (0, 0, 1)])
turtle.done()


