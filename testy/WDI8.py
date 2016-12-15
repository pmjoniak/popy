def f(n):
	if n == 1:
		return 1
	return n + f(n - 1)


def f2(n):
	if n == 1:
		return 0
	if n % 2 == 0:
		return f2(n // 2) + 1
	return f2((n + 1) // 2) + 1


def f3(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return 2 * f3(n // 2) + 1
	return f3((n + 1) // 2) + f3((n - 1) // 2) + 1


L = []
def hanoi(a, b, c, ile):
	if ile == 1:
		L.append((a, b))
		return
	hanoi(a, c, b, ile - 1)
	L.append((a, b))
	hanoi(c, b, a, ile - 1)


hanoi('a', 'b', 'c', 4)
print(L)


print(f(32))
print(f2(32))
print(f3(32))