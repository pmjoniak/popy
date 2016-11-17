from turtle import *
import random

BOK = 15
tracer(0,1)
SX = 0
SY = 0

def kwadrat(x, y, kolor):
  fillcolor(kolor)
  pu()
  goto(SX + x * BOK, SY + y * BOK)
  pd()
  begin_fill()
  for i in range(4):
    fd(BOK)
    rt(90)
  end_fill() 

def rysuj(T):
  clear()
  for y in range(len(T)):
    for x in range(len(T[y])):
      if T[y][x] == '#':
        kolor = 'blue'
      elif T[y][x] == '*':
        kolor = 'green'
      elif T[y][x] == '@':
        kolor = 'red'
      elif T[y][x] == '&':
        kolor = 'orange'
      else:
        kolor = 'white'
      kwadrat(x, y, kolor)
  update()    
      
        
def tablica(M, N):
  T = []
  for i in range(M):
    T.append( N * [0] )
  return T  
  
def sasiedzi(x,y, MX, MY, zawijaj = True):
  wynik = []
  for dx,dy in [ (-1,-1), (-1,1), (1,1), (1,-1), (1,0), (0,1), (-1,0), (0,-1)]:
    
    if zawijaj or (x+dx >= 0 and x+dx<MX and y+dy >= 0 and y+dy<MY):
      nx = (x+dx) % MX
      ny = (y+dy) % MY
      wynik.append( (nx,ny) )
  return wynik
  
def nowe_pokolenie(T, kolor, zawijaj = True):
  MY = len(T)
  MX = len(T[0])
  N = tablica(MY, MX)
  for y in range(MY):
    for x in range(MX):
      L = []
      for nx,ny in sasiedzi(x,y, MX, MY, zawijaj):
        if T[ny][nx] != '.':
          L.append(T[ny][nx])
      if T[y][x] != '.' and len(L) in [2,3]:
        if kolor == 2:
          N[y][x] = '#'        
        else:
          N[y][x] = T[y][x]
      elif T[y][x] != '.':
        N[y][x] = '.'
      elif T[y][x] == '.' and len(L) == 3:
        if kolor == 3:
          N[y][x] = sorted(L)[1]
        elif kolor == 4:
          if len(set(L)) == 3:
            N[y][x] = list({'#', '*', '@', '&'} - set(L))[0]
          else:
            N[y][x] = sorted(L)[1]
        else:
          N[y][x] = '#'
      else:
        N[y][x] = '.'
  return N
         

def nowe_pokolenie2(T, zycie, narodziny, zawijaj = True):
  MY = len(T)
  MX = len(T[0])
  N = tablica(MY, MX)
  for y in range(MY):
    for x in range(MX):
      L = []
      for nx,ny in sasiedzi(x,y, MX, MY, zawijaj):
        if T[ny][nx] != '.':
          L.append(T[ny][nx])
      if T[y][x] != '.' and len(L) in zycie:
        N[y][x] = T[y][x]
      elif T[y][x] != '.':
        N[y][x] = '.'
      elif T[y][x] == '.' and len(L) in narodziny:
        N[y][x] = '#'
      else:
        N[y][x] = '.'
  return N         


def is_dead(kolonia):
  MY = len(kolonia)
  MX = len(kolonia[0])
  N = tablica(MY, MX)
  for y in range(MY):
    for x in range(MX):
      if kolonia[y][x] != '.':
        return False
  return True


kolonia = """
................
................
......**#.......
.....#**........
................
................
...........&#@..
.............@..
...........&....
""".split()[::-1]

kolonia = """
................
................
................
................
................
................
...........###..
.............#..
............#...
""".split()[::-1]



kolonia = list(map(list, kolonia))
historia = {}

okres = 1
while True:
  rysuj(kolonia)
  if is_dead(kolonia):
    print('okres', 0)
    break
  h = ''.join(sum(kolonia,[]))
  if h in historia.keys():
    o = (okres - historia[h])
    print('okres', o)
    break
  historia[h] = okres
  okres += 1
  kolonia = nowe_pokolenie(kolonia, 3, True)

done()