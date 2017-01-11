def ppn(s):
	L = []
	D = {}
	n = 1
	for a in s:
		if a not in D:
			D[a] = str(n)
			n += 1
		L.append(D[a])

	return '-'.join(L)

print(ppn('indianin'))
