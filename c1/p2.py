def silnia(n):
	wynik = 1
	for i in range(2, n + 1):
		wynik *= i
	return wynik


for i in range(4, 101):
	cyfr = len(str(silnia(i)))
	print(i, "! ma ", cyfr, " ", end='')
	if cyfr % 10 in range(2, 5) and (cyfr % 100) not in range(12, 15):
		print('cyfry')
	else:
		print('cyfr')
