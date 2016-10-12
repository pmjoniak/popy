import math


def kolko(n, l=0):
	for x in range(1, n + 1):
		print(' ' * l, end='')
		for y in range(1, n + 1):
			if math.sqrt((x - 0.5 - n / 2) * (x - 0.5 - n / 2) + (y - 0.5 - n / 2) * (y - 0.5 - n / 2)) <= n / 2:
				print('*', end='')
			else:
				print(' ', end='')
		print('')


kolko(7, 3)
kolko(9, 2)
kolko(11, 1)
kolko(13, 0)
