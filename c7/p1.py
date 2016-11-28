def litery(wyraz):
	wynik = {}
	for c in wyraz:
		if c not in wynik:
			wynik[c] = 1
		else:
			wynik[c] += 1
	return wynik


def ukldalne(w1, w2):
	l1 = litery(w1)
	l2 = litery(w2)
	for e in l1:
		if e not in l2:
			return False
		if l1[e] > l2[e]:
			return False
	return True


print(ukldalne('kot', 'kałasznikowt'))