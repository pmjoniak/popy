import math
import time


def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n)), 2):
		if n % i == 0:
			return False
	return True


def isHappy(n, what_is_true_happines):
	return what_is_true_happines in str(n)


def maybePrime(n):
	for i in [2, 3, 5, 7]:
		if n % i == 0:
			return False
	return True


# count = 0
# for n in range(1, 100000):
# 	if isHappy(n, '777') and isPrime(n):
# 		count += 1
# 		print(n)
# print('Znaleziono ', count, ' szczesliwych')

# count = 0
# start = time.time()
# for n in range(9999999999, 1, -2):
# 	if isPrime(n) and isHappy(n, '7777777'):
# 		print(n)
# 		break
# print('a trwalo to ', time.time() - start, 's', sep='')

can = []
for i in range(1000):
	s = str(i)
	if len(s) < 3:
		s = '{:03}'.format(i)
	for j in range(4):
		ss = s[:j] + '7777777' + s[j:]
		if len(str(int(ss))) == 10:
			can.append(int(ss))
print(len(can))
can = sorted(set(can))
print(len(can))

start = time.time()
count = 0
for n in can:
	if isPrime(n):
		#print(n)
		count += 1

print('a trwalo to ', time.time() - start, 's', sep='')
print('a jest ich', count)
