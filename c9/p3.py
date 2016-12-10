
slownik = {}
for wiersz in open("../c6/slowa.txt", encoding='utf-8'):
	slownik[wiersz[:-1].lower()] = 1

max_len = -1
max_txt = ''
text = open("tekst.txt", encoding='utf-8').read().split()

curr_len = 0
curr_txt = ''
for wyraz in text:
	if len(wyraz.encode()) != len(wyraz):
		if curr_len > max_len:
			max_len = curr_len
			max_txt = curr_txt
		curr_txt = ''
		curr_len = 0
		continue
	curr_txt = curr_txt + ' ' + wyraz
	for c in ',.()!?':
		wyraz.replace(c, '')
	curr_len = curr_len + len(wyraz)

print(max_txt)