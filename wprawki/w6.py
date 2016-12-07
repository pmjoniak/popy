def scal(L1, L2):
	L = []
	i = 0
	j = 0
	while i < len(L1) and j < len(L2):
		if (L1[i] < L2[j]):
			L.append(L1[i])
			i += 1
		else:
			L.append(L2[j])
			j += 1
	for k in range(i, len(L1)):
		L.append(L1[k])
	for k in range(j, len(L2)):
		L.append(L2[k])
	return L


def scalanie(L):
	if len(L) == 1:
		return L
	k = len(L) // 2
	L1 = scalanie(L[:k])
	L2 = scalanie(L[k:])
	return scal(L1, L2)


L = [9, 8, 7, 6, 1, 4, 3, 2, 2, 1, 5, 4, 3, 2, 1]
print(scalanie(L))
print(sorted(L))
print(scalanie(L) == sorted(L))
