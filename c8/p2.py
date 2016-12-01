program = []
etykiety = {}
import sys

for x in open('prog.pygo'):
	L = x.split()
	if len(L) == 0:
		continue
	if L[0][-1] == ':':
		etykiety[L[0][:-1]] = len(program)
		L = L[1:]
	if L[0] == 'goto':
		program.append( ('goto', L[1]))
	elif L[0] == 'print':
		program.append( ('print', ' '.join(L[1:])))
	elif L[1] == '=':
		program.append( ('=', L[0], ' '.join(L[2:])))
	elif L[0] == 'if':
		program.append( ('if', ' '.join(L[1:-2]), L[-1]))    
	else:
		program.append( ('error',-1) )  
		
#for p in program:
#  print (p)
#print(etykiety)

PC = 0
E = {}

while PC < len(program):
	p = program[PC]
	if p[0] == 'goto':
		PC = etykiety[p[1]]
	elif p[0] == '=':
		E[p[1]] = eval(p[2], E)
		PC += 1
	elif p[0] == 'print':
		print( eval(p[1],E) )
		PC += 1
	elif p[0] == 'if':
		if eval(p[1], E) == True:
			PC = etykiety[p[2]]
		else:
			PC += 1
	else:
		print ('Nieznana instrukcja', p)    