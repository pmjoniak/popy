import collections
import random

imiona = []
litery = set('chrzańufnąbelgijskośćtępwyżmłódź')
# litery = set('acgwel')


for x in open('imiona.txt', encoding='utf-8'):
	x = x[:-1]
	imiona.append(x.lower())


# imiona = ['pawel', 'ewedina']
print(len(imiona))
print(len(imiona) * len(litery) ** 2)
print(len(litery) ** 3)


def findAll(S, sub):
	index = 0
	res = []
	while index < len(S):
		index = S.find(sub, index)
		if index == -1:
			break
		res.append(index)
		index += len(sub)
	return res


staty = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))

for l1 in litery:
	for l2 in litery:
		para = l1 + l2
		for imie in imiona:
			for idx in findAll(imie, para):
				if idx >= 0 and (idx + 2) < len(imie):
					staty[para][imie[idx + 2]] += 1

for l1 in litery:
	for i in imiona:
		for f in findAll(i, l1):
			if f >= 0 and (f + 1) < len(i):
				staty[l1][i[f + 1]] += 1

#print(staty)
for para in staty:
	s = sum(staty[para].values())
	for l in staty[para]:
		staty[para][l] /= s


def daj_imie():
	imie = random.choice(list(litery))
	dlugosc = random.randint(4, 10)
	i = 1
	while i < dlugosc:
		# print(imie, i)
		prev = imie[i - 1]
		if i > 1:
			prev = imie[i - 2] + prev
		p = random.random()
		suma = 0
		# print(staty[prev], p)
		if len(staty[prev]) == 0:
			return imie
		for mozliwosc in staty[prev]:
			suma += staty[prev][mozliwosc]
			if suma > p:
				imie += mozliwosc
				i += 1
				break
	return imie

for i in range(100):
	print(daj_imie())
