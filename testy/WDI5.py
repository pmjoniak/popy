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
	return fTrec(n - 1, m) + 2 * fTrec(n, m - 1)


def fTiter(n, m):
	L = (n + m + 1) * [0]
	for i in range(n + m):
		for j in range(i + 1, -1, -1):
			xm = j
			xn = i + 1 - j
			if j == i + 1:
				L[j] = L[j - 1] + 1
			elif j == 0:
				L[j] = L[j] + 1
			else:
				L[j] = L[j] + 2 * L[j - 1]
			if xn == n and xm == m:
				return L[j]


count = 0
def pot(a, b):
	rez = 1
	global count
	while b > 0:
		if b % 2:
			count += 1
			rez = rez * a
		b = b // 2
		a = a * a
		count += 1
	return rez


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
print(fTrec(15, 9))
print(fTiter(15, 9))
# print(fib(23) % 10)
# print(maximum1)
# print(fibMod(23, 10))
# print(maximum2)
# print(findK(3, 12345678))
# pot(5, 1023)
# print(count)