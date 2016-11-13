def F(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1


def energia(n):
	if n == 1:
		return 0
	count = 0
	while n != 1:
		n = F(n)
		count += 1
	return count


def analiza(a, b):
	L = []
	for n in range(a, b + 1):
		L.append(energia(n))
	avg = sum(L) / len(L)
	med = sorted(L)[int(len(L) / 2)]
	minimum = sorted(L)[0]
	maximum = sorted(L)[-1]
	print('avg', avg, 'med', med, 'min', minimum, 'max', maximum)


print(energia(7))
analiza(1, 7)
