from card import card

import random


class deck:
	'''
		self.index: current position in the deck
		self.cutpoint: suggested to stop using this deck
		deck is maintained by a list
	'''
	def __init__(self, num):
		'''
			initialize the deck with number of decks
			set cutpoint to 0.8 of decks
 		'''
		self.num = num
		values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
		suits = ['H','S','D','C']
		self.deck = []
		for i in range(num):
			for value in values:
				for suit in suits:
					self.deck.append(card(value,suit))

		random.shuffle(self.deck)
		self.cutpoint = self.num * 52 * 0.8
		self.index = 0

	def get_next(self):
		'''
			return [card, boolean]
			boolean indicates whether you need shuffle or not
		'''
		next_card = self.deck[self.index]
		self.index += 1
		if self.index > self.cutpoint:
			need_shuffle = True
		else:
			need_shuffle = False
		return [next_card,need_shuffle]

	def get_deck(self):
		return self.deck


if __name__ == "__main__":
	pass
	#d = deck(8)
	#for i in range(400):
	#	print(d.get_next()[0])
		
