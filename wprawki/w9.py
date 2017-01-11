words = set(open('popularne_slowa.txt').read().split())
P = set()

for w in words:
	for i in range(1, len(w)):
		P.add(w[:i])  # maybe i+1


T1 = ['balEIN', 'dROrkA', 'oPGraW', 'boRAMO', 'arutak', 'szumet']
T = []
for s in T1:
	T.append(s.lower())

print(len(P))


def getN(pos):
	L = []
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			xx = pos[0] + x
			yy = pos[1] + y
			if x != 0 or y != 0:
				if (xx >= 0 and xx <= 5 and yy >= 0 and yy <= 5):
					L.append((xx, yy))
	return L


S = set()

def idi(w, visited, pos):
	visited.add(pos)
	for n in getN(pos):
		if n in visited:
			continue
		let = T[n[1]][n[0]]
		candidate = w + let
		if candidate in words:
			print(candidate)
			S.add(candidate)
			idi(candidate, set(visited), n)
		elif candidate in P:
			idi(candidate, set(visited), n)


for x in range(6):
	for y in range(6):
		idi(T[y][x], set(), (x, y))
print(len(S))
print(sorted(S, key=lambda x:-len(x)))