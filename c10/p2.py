import collections

def zmienne(F):
	return set(F) - set(' +-=()*')


def dict_add(D, k, v):
	D = dict(D)
	D[k] = v
	return D


def zerowalne(F):
	res = collections.defaultdict(lambda: True)
	Z = zmienne(F)
	for i in range(len(F)):
		if F[i] in Z:
			if i > 0 and F[i - 1] in Z:
				res[F[i]] = res[F[i]]
			else:
				res[F[i]] = False
	return res


def wartosciowanie(Z, moze_zero):
	if len(Z) == 0:
		return [{}]
	Z = list(Z)
	z = Z[0]
	W = wartosciowanie(Z[1:], moze_zero)
	startowe = set('0123456789')
	if not moze_zero[z]:
		startowe = startowe - {'0'}
	res = []
	for w in W:
		wolne = startowe - set(''.join(w.values()))
		for val in wolne:
			res.append(dict_add(w, z, val))
	return res
	# return [dict_add(d, z, val) for d in W for val in range(2)]


def zliczbuj(F, w):
	F2 = F
	for k in w:
		F2 = F2.replace(k, w[k])
	return F2


def znajdz(F):
	Z = zmienne(F)
	moze_zero = zerowalne(F)
	W = wartosciowanie(Z, moze_zero)
	for w in W:
		if eval(zliczbuj(F, w)):
			print(zliczbuj(F, w))
			# return w
	return None


# print(len(wartosciowanie(zmienne('send + more == money'))))
# print(wartosciowanie(zmienne('se + mo == mo'), zerowalne('se + mo == mo')))
# print(zliczbuj('send + more', wartosciowanie(zmienne('send + more'))[30]))
# print(zerowalne('send + more == money'))
print(znajdz('send + more == money'))
print(znajdz('ciacho + ciacho == nadwaga'))
