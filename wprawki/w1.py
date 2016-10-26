

def rysuj_kwadraty(n, Duzy, Maly):
	duzy_1 = '#' + (' ' * (Duzy - 2)) + '#'
	maly_1 = '#' + (' ' * (Maly - 2)) + '#'
	print(('#' * Duzy + ' ' * Maly) * (n // 2) + (n % 2) * Duzy * '#')
	for i in range(Duzy - Maly - 1):
		print((duzy_1 + ' ' * Maly) * (n // 2) + (n % 2) * duzy_1)
	print((duzy_1 + '#' * Maly) * (n // 2) + (n % 2) * duzy_1)
	for i in range(Maly - 2):
		print((duzy_1 + maly_1) * (n // 2) + (n % 2) * duzy_1)
	print('#' * (Duzy + Maly) * (n // 2) + (n % 2) * Duzy * '#')


rysuj_kwadraty(5, 8, 4)

