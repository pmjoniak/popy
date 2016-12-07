import random
import collections

pol_ang = collections.defaultdict(lambda: [])
brown = collections.defaultdict(lambda: 0)

for x in open('pol_ang.txt', encoding='utf-8'):
    x = x[:-1]
    wiersz = x.split('=')
    if len(wiersz) != 2:
        continue
    pol, ang = wiersz
    pol_ang[pol].append(ang)

for x in open('brown.txt', encoding='utf-8'):
    x = x[:-1]
    wiersz = x.split(' ')
    for w in wiersz:
        brown[w] += 1


def tlumacz(L):
    wynik = []
    for w in L:
        if w in pol_ang:
            tr = sorted(pol_ang[w], key=lambda a: -brown[a])[0]
            wynik.append(tr)
        else:
            wynik.append('?' + w)
    return wynik


for wiersz in open('text.txt', encoding='utf-8'):
    wiersz = wiersz.split()
    print(' '.join(tlumacz(wiersz)))