import math


def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n)), 2):
		if n % i == 0:
			return False
	return True


def pierwsze(n):
	L = []
	for i in range(2, n + 1):
		if isPrime(i):
			L.append(i)
	return L


def wystapienia(x, p):
	licznik = 0
	while x % p == 0:
		licznik += 1
		x = x // p
	return licznik


def wystapieniaS(S, p):
	return sum(map(lambda x: wystapienia(x, p), S))


def wszystkieWystapienia(S):
	maximum = max(S)
	primes = pierwsze(maximum)
	result = {}
	for p in primes:
		ile = wystapieniaS(S, p)
		if ile > 0:
			result[p] = ile
	print(result)
	return result


def najpopularniejsza(S):
	maximum = 0
	naj = -1
	for s in wszystkieWystapienia(S).items():
		if s[1] > maximum:
			maximum = s[1]
			naj = s[0]
	return naj


print(najpopularniejsza([123233, 13231, 5621, 1237]))
