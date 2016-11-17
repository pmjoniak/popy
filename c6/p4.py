
def findInData(data, v, a, b):
	while True:
		# print(a, b)
		if a == b:
			if data[a] == v:
				return True
			else:
				return False
		if b == a + 1:
			if data[a] == v or data[b] == v:
				return True
			else:
				return False
		c = (a + b) // 2
		if data[c] == v:
			return True
		elif data[c] < v:
			a = c + 1
		else:
			b = c - 1


f = open("slowa.txt", 'r', encoding='utf-8')
data = f.read().splitlines()
datas = sorted(data)

for i in range(len(datas)):
	s = datas[i]
	sr = s[::-1]
	# if i % 1000 == 0: 
	#	print(i)
	if findInData(datas, sr, 0, len(datas)):
		print(s, '-', sr)
