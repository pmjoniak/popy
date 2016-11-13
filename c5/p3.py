def only_one(L):
	if L == []:
		return []
	L2 = sorted([(L[i], i) for i in range(len(L))])
	# print(L2)
	unique = [L2[0][::-1]]
	for e in L2[1:]:
		if e[0] != unique[-1][1]:
			unique.append(e[::-1])
	# print(unique)
	unique.sort()
	# print(result)
	result = []
	for e in unique:
		result.append(e[1])
	return result


print(only_one([4, 4, 5, 3, 3, 6, 9, 7, 1, 1]))

