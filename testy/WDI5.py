def silniowa(n):
	silnia = 1
	mnoznik = 2
	while silnia * mnoznik < n:
		silnia = silnia * mnoznik
		mnoznik += 1
	L = []
	mnoznik -= 1
	while mnoznik > 0:
		L.append(n // silnia)
		n = n - (n // silnia) * silnia
		silnia = silnia // mnoznik
		mnoznik -= 1
	return L


def gdc(n, m):
	if n < m:
		n, m = m, n
	mnoznik = 1
	while m != 0:
		if n < m:
			n, m = m, n
		ilenp = n % 2 + m % 2
		if ilenp == 2:
			n = n - m
		if ilenp == 0:
			mnoznik *= 2
			n = n // 2
			m = m // 2
		if n % 2 == 0:
			n = n // 2
		else:
			m = m // 2
	return mnoznik * n


maximum1 = 0
def fib(n):
	if n <= 2:
		return 1
	nowy = fib(n - 1) + fib(n - 2)
	global maximum1
	maximum1 = max(maximum1, nowy)
	return nowy


maximum2 = 0
def fibMod(n, r):
	if n <= 2:
		return 1
	nowy = fibMod(n - 1, r) + fibMod(n - 2, r)
	global maximum2
	maximum2 = max(maximum2, nowy)
	return nowy % r


def fTrec(n, m):
	if n == 0:
		return m
	if m == 0:
		return n
	return fTrec(n - 1, m) + 2 * fTrec(m, m - 1)


def fTiter(n, m):
	pass


def findK(n, m):
	if n > m:
		return 1
	L = []
	licznik = 1
	i = 0
	while n < m:
		L.append((licznik, n))
		licznik *= 2
		n *= n
		i += 1
	# print(L)
	suma = 0
	i -= 1
	iloczyn = 1
	# print(i)
	while i >= 0:
		if m > iloczyn * L[i][1]:
			iloczyn *= L[i][1]
			suma += L[i][0]
		i -= 1
	return suma + 1


# print(silniowa(100))
# print(gdc(4, 100))
# print(fTrec(15, 5))
# print(fib(23) % 10)
# print(maximum1)
# print(fibMod(23, 10))
# print(maximum2)
# print(findK(3, 12345678))
