def sublist(L):
	if len(L) == 0:
		return [[]]
	sub = sublist(L[1:])
	add = [s + [L[0]] for s in sub]
	return add + sub


def sublist2(L0):
	result = []
	for i in range(2**len(L0)):
		L = []
		for j in range(len(L0)):
			if (i & (1 << j)):
				L.append(L0[j])
		result.append(L)
	return result


print(sublist([1, 2, 3, 4]))
print(sublist2(list('asdf')))
