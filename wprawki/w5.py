import random
import sys
import os

talia = [k + n for k in '♠♥♦♣' for n in '23456789TJQKA']


def getHand(talia):
	return random.sample(talia, 13)


faces_points = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
suits_points = {0: 3, 1: 2, 2: 1}


def points(hand):
	print('hand', hand)
	points = 0
	in_suit = {k: 0 for k in '♠♥♦♣'}
	for card in hand:
		if card[1] in faces_points.keys():
			points += faces_points[card[1]]
		in_suit[card[0]] += 1
	print('points from faces', points)
	print('cards in suits', in_suit)
	for k in in_suit.values():
		if k in suits_points.keys():
			points += suits_points[k]
	print('all points', points)

	return points


def nic(*a):
	pass


old_print = print
print = nic

N = 100000
count = 0
for i in range(N):
	if points(getHand(talia)) >= 12:
		count += 1


old_print(count / N)
