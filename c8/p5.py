import random
import itertools
import collections


slowka = []
slownik = {}
slownik_liter = collections.defaultdict(lambda: [])
niepolskie = 'v#|q\'x'
litery = set('chrzańufnąbelgijskośćtępwyżmłódź')

for wiersz in open("../c6/slowa.txt", encoding='utf-8'):
	nie = False
	for s in niepolskie:
		if s in wiersz:
			nie = True
			break
	if nie:
		continue

	w = wiersz[:-1]
	slownik_liter[''.join(sorted(w.lower()))].append(w)
	slowka.append(wiersz[:-1].lower())
	slownik[wiersz[:-1].lower()] = 1

def sublist(L):
	if len(L) == 0:
		return [[]]
	sub = sublist(L[1:])
	add = [s + [L[0]] for s in sub]
	return add + sub


def polafabeton(slowka, slownik, start, dopychaj):
	slowa = start
	niepowodzenie = 0
	while True:
		w = random.choice(slowka)
		razem = ''.join(slowa) + w
		if len(razem) == len(set(razem)):
			slowa.append(w)
			niepowodzenie = 0
			if len(razem) == 32:
				return slowa
		else:
			niepowodzenie += 1
		if niepowodzenie > 100:
			break
	if not dopychaj:
		return slowa
	while True:
		brak = ''.join(litery - set(''.join(slowa)))
		kandydaci = sublist(list(brak))
		znalazl = False
		for k in kandydaci:
			w = ''.join(k)
			if len(w) > 0:
				if ''.join(sorted(w)) in slownik_liter.keys():
					slowa.append(random.choice(slownik_liter[''.join(sorted(w))]))
					znalazl = True
					break
		if not znalazl:
			return slowa
	# while True:
	# 	brak = ''.join(litery - set(''.join(slowa)))
	# 	if len(brak) == 0:
	# 		return slowa
	# 	kandydaci = sublist(list(brak))
	# 	znalazl = False
	# 	for k in kandydaci:
	# 		w1 = ''.join(k)
	# 		for w in itertools.permutations(w1):
	# 			if len(w) > 0 and w in slownik.keys():
	# 				slowa.append(w)
	# 				znalazl = True
	# 				break
	# 	if not znalazl:
	# 		return slowa


trudnosc = {a: 0 for a in litery}

N = 1000
for i in range(N):
	pa = polafabeton(slowka, slownik, [], True)
	brak = litery - set(''.join(pa))
	for l in brak:
		trudnosc[l] += 1
	if i % (N // 100) == 0:
		print(100 * i / N)
	# print(pa)
	# print(brak)

print(sorted(trudnosc.items()))


def trudnoscSlowa(w):
	if len(w) != len(set(w)):
		return 1
	suma = 0
	for l in w:
		if l not in trudnosc.keys():
			return 1
		suma += trudnosc[l]
	return -suma / len(w)


trudneSlowa = sorted(slowka, key=trudnoscSlowa)

trudneSlowka = trudneSlowa[:500]
trudneSlownik = {w: 1 for w in trudneSlowka}
print(sorted(trudneSlowka))


alfa = []
minimum = 32
for i in range(10000):
	start = polafabeton(trudneSlowka, trudneSlownik, [], False)
	pa = polafabeton(slowka, slownik, start, True)
	# pa = polafabeton(slowka, slownik, [trudneSlowa[random.randint(0, 100)]], True)
	brak = litery - set(''.join(pa))
	if len(brak) < minimum:
		print(len(brak), brak, pa)
		minimum = len(brak)
	if len(brak) == 0:
		print("ALFABETON: ", end='')
		alfa.append(pa)
		print(len(brak), brak, pa)
	# print(brak)trudneSlowa[random.randint(0, 10)]


print("ALFABETONY: ")
for a in alfa:
	print(a)
