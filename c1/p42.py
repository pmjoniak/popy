from losowanie_fragmentow import losuj_fragment

def haslo(n):
	result = ""
	while(n-len(result) > 4):
		result += losuj_fragment()
	
	diff = n-len(result)
	s=""	
	while(len(s) != diff):
		s = losuj_fragment()
	result += s;
	return result


print(haslo(8))
print(haslo(10))
print(haslo(12))
