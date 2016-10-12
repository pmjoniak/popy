def koperta(n):
	print('*' * (2 * n + 1))
	for y in range(1, 2 * n):
		for x in range(2 * n + 1):
			if (x == 0 or x == 2 * n or x == y or (2 * n - x) == y):
				print('*', end='')
			else:
				print(' ', end='')
		print('')
	print('*' * (2 * n + 1))


koperta(4)
