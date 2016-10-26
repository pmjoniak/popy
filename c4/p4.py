import random
import math


def mieszaj(L):
	kopia = L[:]
	wynik = []
	for i in range(len(L) - 1, -1, -1):
		idx = random.randint(0, i)
		wynik.append(kopia[idx])
		kopia[i], kopia[idx] = kopia[idx], kopia[i]
	return wynik


def randperm(n):
	L = list(range(n))
	return mieszaj(L)


count = 0
N = 1000000
n = 5
ex = list(range(n))

for i in range(N):
	if(randperm(n) == ex):
		count += 1
print('procent 1 permutacji', 100 * count / N)
print('a powinno byc', 100 / math.factorial(n))
