import copy


def only_one(L):
	if L == []:
		return []
	result = [L[0]]
	z = set(result)
	for e in L[1:]:
		if e not in z:  # not (e in result)
			result.append(e)
			z.add(e)
	return result


N = 10000000
# list(set(list(range(N))))
# only_one(list(range(N)))

L = 5 * [0]
for i in range(5):
	L[i] = 3 * [0]
print(L)

L2 = copy.deepcopy(L)
print(L2)

for i in range(len(L)):
	for j in range(len(L[i])):
		L[i][j] = i*3+j
		print(L[i][j], end='')
	print('')

print(L)
print(L2)
