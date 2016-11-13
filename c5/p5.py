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


def stworzPalete(prog, kolory):
	L = []
	poprzedni_kolor = 0
	count = 0
	for x in prog:
		if x == 'f':
			count += 1
		elif x in '0123456789':
			poprzedni = kolory[poprzedni_kolor]
			nastepny = kolory[int(x)]
			if count == 1:
				L.append(mieszanina(poprzedni, nastepny, 0.5))
			else:
				for i in range(count):
					nowy = mieszanina(poprzedni, nastepny, i / (count - 1))
					L.append(nowy)
			count = 0
			poprzedni_kolor = int(x)
	if count > 0:
		for i in range(count):
			L.append(kolory[poprzedni_kolor])
	print(L)
	return L


def murek(prog, kolory):
	paleta = stworzPalete(prog, kolory)
	count = 0
	rysuj = True
	for x in prog:
		if x == 'f':
			if rysuj:
				kwadrat(BOK, paleta[count])
			count += 1
			fd(BOK)
		elif x == 'b':
			bk(BOK)
		elif x == 'r':
			rt(90)
			fd(BOK)
		elif x == 'l':
			bk(BOK)
			lt(90)
		elif x == 'u':
			rysuj = False
			pu()
		elif x == 'd':
			rysuj = True
			pd()


tracer(0, 0)
prog = 'u' + 15 * 'b' + 'ld' + 30 * ('0' + 5 * 'f' + '' + 5 * 'f' + '2u' + 10 * 'b' + 'rfld')
print(prog)
murek(prog, [(1, 0, 0), (1, 0.7, 0.7), (1, 1, 1)])
update()
done()
