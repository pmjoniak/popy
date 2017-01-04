def kompozycja(A, znaki):
	if len(A) == 0:
		return ['']
	a = A[0]
	reszta = kompozycja(A[1:], znaki)
	L = []
	for r in reszta:
		for z in znaki:
			if len(r) == 0:
				z = ''
			L.append(a + z + r)
			L.append('-' + a + z + r)
	return L
	# return [a + z + r for r in reszta ]


def my_eval(s):
	try:
		return eval(s)
	except Exception as e:
		return 0


def kompozycja2():
	L1 = set([eval(k) for k in kompozycja(['2'], ['*', '**', '/', '+', '-', ''])])
	L2 = set([eval(k) for k in kompozycja(['2'], ['*', '**', '/', '+', '-', ''])])
	L3 = set([eval(k) for k in kompozycja(['2', '2'], ['*', '**', '/', '+', '-', ''])])
	print(L1)
	print(L2)
	print(L3)
	for a1 in L1:
		for a2 in L2:
			for a3 in L3:
				L = kompozycja([str(a1), str(a2), str(a3)], ['+', '-', '*', '**', '/'])
				L.append(kompozycja([str(a1), str(a3), str(a2)], ['+', '-', '*', '**', '/']))
				L.append(kompozycja([str(a2), str(a1), str(a3)], ['+', '-', '*', '**', '/']))
				L.append(kompozycja([str(a2), str(a3), str(a1)], ['+', '-', '*', '**', '/']))
				L.append(kompozycja([str(a3), str(a2), str(a1)], ['+', '-', '*', '**', '/']))
				L.append(kompozycja([str(a3), str(a1), str(a2)], ['+', '-', '*', '**', '/']))
				EL = [my_eval(k) for k in L if my_eval(k) >= 2017 and my_eval(k) <= 10000]
				if len(EL) != 0:
					print(a1, a2, a3, min(EL))


def kompozycja3(a, b):
	L1 = set([eval(k) for k in kompozycja(a * ['2'], ['*', '**', '/', '+', '-', ''])])
	L2 = set([eval(k) for k in kompozycja(b * ['2'], ['*', '**', '/', '+', '-', ''])])
	print(L1)
	print(L2)
	for a1 in L1:
		for a2 in L2:
			L = kompozycja([str(a1), str(a2)], ['+', '-', '*', '**', '/'])
			L.append(kompozycja([str(a2), str(a1)], ['+', '-', '*', '**', '/']))
			EL = [my_eval(k) for k in L if my_eval(k) >= 2017 and my_eval(k) <= 10000]
			if len(EL) != 0:
				print(a1, a2, min(EL))


#print(kompozycja(['2', '2', '2'], ['*', '**', '/', '+', '-', '']))
#L = kompozycja(['2', '2', '2', '2'], ['*', '**', '/', '+', '-', ''])
#print([eval(k) for k in L if eval(k) >= 2017 and eval(k) <= 10000])
#kompozycja3(2, 2)
#kompozycja3(1, 3)
kompozycja2()