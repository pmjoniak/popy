import collections
import itertools


slowka = []
slownik_liter = collections.defaultdict(lambda: [])
niepolskie = 'v#|q\'x'

for wiersz in open("../c6/slowa.txt", encoding='utf-8'):
	nie = False
	for s in niepolskie:
		if s in wiersz:
			nie = True
			break
	if nie:
		continue

	w = wiersz[:-1].lower()
	slownik_liter[''.join(sorted(w.lower()))].append(w)
	slowka.append(wiersz[:-1].lower())


def litery(wyraz):
	wynik = {}
	for c in wyraz:
		if c not in wynik:
			wynik[c] = 1
		else:
			wynik[c] += 1
	return wynik


def ukladalne(w1, w2):
	l1 = litery(w1)
	l2 = litery(w2)
	# print(l1, l2)
	for e in l1:
		if e not in l2:
			return False
		if l1[e] > l2[e]:
			return False
	return True


def filtruj(osoba, data):
	L = []
	for w1 in data:
		if ukladalne(w1.lower(), osoba):
			L.append(w1.lower())
	return L


def brakuje(jest, ma_byc):
	res = ''
	l1 = litery(jest)
	l2 = litery(ma_byc)
	for e in l2:
		if e not in l1:
			res = res + l2[e] * e
		else:
			res = res + (l2[e] - l1[e]) * e
	return res


def add(w1, w2, w3, S):
	L = [w1, w2, w3]
	for p in itertools.permutations(L):
		if ' '.join(L) in S:
			return
	S.add(' '.join(L))


def anagramy(imie, nazwisko):
	osoba = (imie + nazwisko).lower()
	slowa = filtruj(osoba, slowka)
	print(len(slowa))
	S = set()
	for w1 in slowa:
		for w2 in slowa:
			if len(w1 + w2) < len(osoba):
				if ukladalne(w1 + w2, osoba):
					brak = brakuje(w1 + w2, osoba)
					brak = ''.join(sorted(brak))
					if brak in slownik_liter:
						for w3 in slownik_liter[brak]:
							add(w1, w2, w3, S)
	return S


# print(ukladalne('wsparł', 'bolesławprus'))
# A = anagramy('bartosz', 'witkowski')
A = anagramy('paweł', 'joniak')
print(A)
