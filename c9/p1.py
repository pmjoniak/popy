from turtle import *
import random

speed('fastest')

BOK = 15
tracer(0,1)
MAX = 20
kolory = ['red', 'green', 'yellow', 'blue', 'pink', 'orange', 'cyan']

def kwadrat(x,y,bok, kolor):
   fillcolor(kolor)
   pu()
   goto(x * bok-100, -y * bok+100)
   pd()

   begin_fill()
   for i in range(4):
     fd(bok)
     rt(90)
   end_fill()


def sasiedzi(x,y, Max):
  res = []
  Min = 0
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      if (dx,dy) != (0,0):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < Max and 0 <= ny < Max:
          res.append( (nx,ny) )
  return res

T = {}
for i in range(15):
  x = random.randint(0,MAX-1)
  y = random.randint(0,MAX-1)
  T[x,y] = random.choice(kolory)

H = {}
i = 0;
while (True):
  for x,y in T:
    if (x, y) not in H or H[x,y] != T[x,y]:
      kwadrat(x,y, BOK, T[x,y])
      H[x, y] = T[x, y]
  N = {}
  for x,y in T:
    nx,ny = random.choice(sasiedzi(x,y,MAX))
    N[nx,ny] = T[x,y]

  x = random.randint(0,MAX-1)
  y = random.randint(0,MAX-1)
  N[x,y] = random.choice(kolory)
  T = N
  update()
  i = i + 1
  if i % 100 == 0:
    clear()
    for x,y in H:
      kwadrat(x,y, BOK, H[x,y])
    update()
  # clear()

x = input()
