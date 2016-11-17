f = open("slowa.txt", 'r', encoding='utf-8')
data = f.read().splitlines()

# nowe = []
# for s in data:
# 	nie_ma = True
# 	for c in s:
# 		if c in 'ąęółśżźćńąĄĘÓŁŚŻŹĆŃ':
# 			nie_ma = False
# 			break
# 	if nie_ma:
# 		nowe.append(s)
nowe = list(filter(lambda x: len(x.encode()) == len(x), data))
posortowane = sorted(nowe, key=lambda x: (-len(x), -len(set(x)) / len(x)))
print(posortowane[0:10])
print(sorted(nowe, key=lambda x: len(set(x)) / len(x))[0:10])
