letters = list('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')
positions = {a: b for a, b in zip(letters, range(1000))}


def cesar(s, k):
	return ''.join([letters[(positions[b] + k) % len(letters)] for b in s])

print(cesar('paweł', 3))