k = """
""".replace('\n','')
#for i in range(4, len(k) - 4):
#	if k[i-4].islower() and k[i-3:i].isupper() and k[i].islower() and k[i+1:i+4].isupper() and k[i+4].islower():
#		print(k[i-4:i+5])

#import urllib3

#p = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

#http = urllib3.PoolManager()
#r = http.request('GET', p+'12345')
#print(r.data)

# print(urllib3.request('GET', 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'))

import pickle

# a = pickle.load( open( "banner.p", "rb" ) )
# for b in a:
# 	for c, i in b:
# 		print(c * i, end='')
# 	print('')

from PIL import Image


# im = Image.open("oxygen.png")
# last = 0
# for i in range(605):
# 	c = im.getpixel((i, 48))[0]
# 	if c != last:
# 		print(chr(c), end='')
# 		last = c

# L = [105, 10, 16, 101, 103, 14, 105, 16, 121]

k = """146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399
""".replace('\n','').split(',')

im = Image.open("good.jpg")
for i in range(len(k)//2):
	x = int(k[2 * i + 0])
	y = int(k[2 * i + 1])
	c = im.getpixel((x, y))
	print(c)

