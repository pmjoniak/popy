f = open("../c6/slowa.txt", encoding='utf-8')
data = f.read().splitlines()


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


def filtruj(osoba):
	L = []
	for w1 in data:
		if ukladalne(w1.lower(), osoba):
			L.append(w1.lower())
	return L


def anagramy(imie, nazwisko):
	osoba = (imie + nazwisko).lower()
	slowa = filtruj(osoba)
	print(len(slowa))
	S = set()
	for w1 in slowa:
		for w2 in slowa:
			if len(w1 + w2) == len(osoba):
				if sorted(w1 + w2) == sorted(osoba):
					if (w1 + ' ' + w2) not in S and (w2 + ' ' + w1) not in S:
						S.add(w1 + ' ' + w2)
	return S


#print(ukladalne('wsparł', 'bolesławprus'))
# A = anagramy('bartosz', 'witkowski')
# A = anagramy('emil', 'barczyński')
A = anagramy('obca', 'makabra')
print(A)

