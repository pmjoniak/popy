def krzyzyk(n):
	for i in range(n):
		print(" " * n + "*" * n + " " * n)
	for i in range(n):
		print("*" * n * 3)
	for i in range(n):
		print(" " * n + "*" * n + " " * n)


krzyzyk(4)
