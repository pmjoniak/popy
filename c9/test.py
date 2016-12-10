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


def litery(wyraz):
	wynik = {}
	for c in wyraz:
		if c not in wynik:
			wynik[c] = 1
		else:
			wynik[c] += 1
	return wynik


def brak(jest, ma_byc):
	res = ''
	l1 = litery(jest)
	l2 = litery(ma_byc)
	for e in l2:
		if e not in l1:
			res = res + l2[e] * e
		else:
			res = res + (l2[e] - l1[e]) * e
	return res


print(brak('ala', 'aglaap'))
