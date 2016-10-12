def szachownica(n, k):
	for i in range(2 * n):
		for l in range(k):
			for j in range(n):
				if i % 2 == 0:
					print(' ' * k + '*' * k, end='')
				else:
					print('*' * k + ' ' * k, end='')
			print('')


szachownica(4, 3)
