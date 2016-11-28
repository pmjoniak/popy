slownik = {}
slowa = []

for wiersz in open("../c6/slowa.txt", encoding='utf-8'):
	slownik[wiersz[:-1]] = 1

for wiersz in open("slowa_testowe.txt", encoding='utf-8'):
	slowa.append(wiersz[:-1])

pary = {}
for a in slowa:
	pary[a] = {}
	for b in slowa:
		pary[a][b] = ""

for a in slowa:
	for b in slowa:
		if a != b:
			for i in range(1, len(b)):
				b1 = b[:i]
				b2 = b[i:]
				w = b1 + a + b2
				if w in slownik.keys():
					print(b1, a, b2)
					pary[a][b] = (b1, a, b2)
					pary[b][a] = (b1, a, b2)


def ileParMaWyraz(a):
	ile = 0
	np = ""
	for w in slowa:
		if pary[a][w] != "":
			ile += 1
			np = w
	return (ile, np)


def nieMaPar(a, b):
	for w in slowa:
		pary[w][a] = ""
		pary[w][b] = ""
		pary[a][w] = ""
		pary[b][w] = ""


print("eliminacja")
elim = 1
while elim < len(slowa):
	cokolwiek = False
	for a in slowa:
		ile, b = ileParMaWyraz(a)
		if ile == elim:
			cokolwiek = True
			print(pary[a][b])
			nieMaPar(a, b)
			break
	if not cokolwiek:
		elim += 1
