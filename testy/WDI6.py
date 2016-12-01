def zad1(a):
	i = len(a) - 1
	x = a[i]
	l = 0
	p = i
	while l < p:
		k = (l + p) // 2
		if a[k] < x:
			l = k + 1
		else:
			p = k
	return l


def select(L):
	n = len(L)
	for i in range(n):
		minimum = i
		for j in range(i + 1, n):
			if L[j] < L[minimum]:
				minimum = j
		L[i], L[minimum] = L[minimum], L[i]
	return L


def babelek(L):
	n = len(L)
	for i in range(n):
		for j in range(i + 1, n):
			if L[i] > L[j]:
				L[i], L[j] = L[j], L[i]
	return L


def wartosc(a):
	k = len(a) - 1
	w = 0
	for i in range(k + 1):
		w = 2 * w + a[i]
	return w


def sito(n):
	L = (n + 1) * [1]
	for i in range(2, n + 1):
		if L[i] == 1:
			print(i)
			for j in range(2 * i, n + 1, i):
				L[j] = 0



print(zad1([2, 3, 3, 3, 3, 4, 5, 1]))
print(select([2, 4, 1, 7, 4, 8, 3, 6, 3]))
print(babelek([2, 4, 1, 7, 4, 8, 3, 6, 3]))
print(wartosc([1, 1, 0, 0]))
sito(100)
