def sublist(L):
	if len(L) == 0:
		return [[]]
	sub = sublist(L[1:])
	return sub + [s + [L[0]] for s in sub]


def sublist2(L):
	if len(L) == 0:
		return {0}
	sub = sublist2(L[1:])
	return sub | {s + L[0] for s in sub}


print(sublist([1, 2, 3]))
print(sorted(sublist2([1, 2, 3, 100])))
