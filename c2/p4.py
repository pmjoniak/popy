from duze_cyfry import dajCyfre


def wypisz(n):
	s = str(n)
	lines = 5 * ['']
	for c in s:
		cyfra = dajCyfre(c)
		for i in range(5):
			lines[i] += cyfra[i] + ' '
	for i in range(5):
		print(lines[i])


wypisz(3.14159265)
