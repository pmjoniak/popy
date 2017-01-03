def normalizuj(F):
	F2 = F
	for s in 'True False ( ) ! + * '.split():
		F2 = F2.replace(s, ' ')
	zmienne = F2.split()
	F = F.replace('+', ' or ')
	F = F.replace('*', ' and ')
	F = F.replace('!', ' not ')
	return zmienne, F


def spelnialna(F):
	zmienne, F = normalizuj(F)
	return any(eval(F, wart) for wart in wartosciowania(zmienne))


def tautologia(F):
	zmienne, F = normalizuj(F)
	return all(eval(F, wart) for wart in wartosciowania(zmienne))


def dict_add(D, k, v):
	D = dict(D)
	D[k] = v
	return D


def wartosciowania(Z):
	if len(Z) == 0:
		return [{}]
	Z = list(Z)
	z = Z[0]
	Ws = wartosciowania(Z[1:])

	return [dict_add(d, z, val) for d in Ws for val in [False, True]]


print(normalizuj('!(p+q+rak) * True'))
print(wartosciowania(normalizuj('!(p+q+rak) * True')[0]))
print(spelnialna('!(p+q+r) * True'))
print(tautologia('!(p+q+rak) * True'))
