from card import *
from deck import deck
import random
import pandas as pd
import pdb

class play:

	


	def __init__(self, bet, card_source = "random"):
		'''
			need to consider the situation when we need to split
			or just duplicate the result after one split??

			self.dealer_cards: dealer cards, initialized to be 2, index 0 shown, index 1 hidden
			self.player_cards: player cards, initialized to be 2
			self.multiple_hands: boolean indicates if we have multiple hands to play
			self.player_number_value: player points (a number or "busted")
			self.dealer_number_value: dealer points (a number or "busted")
		'''
		self.card_source = card_source
		self.dealer_cards = [self.get_next_card(), self.get_next_card()]
		self.player_cards = [[self.get_next_card(), self.get_next_card()]]
		
		# debug code for extreme cases:
		#self.dealer_cards = [card('2','D'), card('A','C')]
		#self.player_cards = [[card('9','D'), card('5','D')]]


		self.hand_number = 1
		self.current_hand = 0
		self.bet = bet

		self.player_number = [number(self.player_cards[self.current_hand][0]) + self.player_cards[self.current_hand][1]]
		self.dealer_number = number(self.dealer_cards[0]) + self.dealer_cards[1]
		self.player_busted = [False]
		self.dealer_busted = False
		self.result = self.bet



	def play(self):
		self.print_current_hand(0)
		if self.check_black_jack():
			return self.result
		self.player_move()
		self.dealer_move()

		
		
		for curr_hand in range(self.hand_number):
			print("In the end: ---")
			self.print_current_hand(curr_hand)
			if self.player_busted[curr_hand]:
				self.result -= self.bet
			elif self.dealer_busted:
				self.result += self.bet
			else:
				if self.player_number[curr_hand] > self.dealer_number:
					self.result += self.bet
				else:
					self.result -= self.bet

		return self.result


	@staticmethod
	def is_blackjack(card1: card, card2: card):
		if card1.is_ten() and card2.is_ace() or card1.is_ace() and card2.is_ten():
			return True
		else:
			return False


	def check_black_jack(self):
		'''
			check if player or dealer has blackjack
			if the player has blackjack and dealer doesn't have, pay 1.5 times the bet
			if the dealer has blackjack and the player doesn't have, get the bet and end this play
			if they both have blackjack, pay 1 times the bet to player
			Return [True, result] if the hand is ended, together with bet result
			Return False if the hand can continue

			TODO?
			INSURANCE OR EVEN MONEY?
		'''
		player_card_one = self.player_cards[self.current_hand][0]
		player_card_two = self.player_cards[self.current_hand][1]
		play_blackjack = play.is_blackjack(player_card_one, player_card_two)
		dealer_blackjack = play.is_blackjack(self.dealer_cards[0], self.dealer_cards[1])

		print("play blackjack: ", play_blackjack)
		print('dealer blackjack: ', dealer_blackjack)

		if play_blackjack and not dealer_blackjack:
			self.result = self.bet * 2.5
			return True
		elif dealer_blackjack and not play_blackjack:
			self.result = 0
			return True
		elif play_blackjack and dealer_blackjack:
			self.result = self.bet * 2
			return True 
		else:
			return False


	def player_hit(self, hand_number):
		new_card = self.get_next_card()
		self.player_cards[hand_number].append(new_card)
		self.player_number[hand_number] += new_card
		if self.player_number[hand_number].busted():
			self.player_busted[hand_number] = True
			print(new_card, 'player busted')
			return False
		return True

	def dealer_hit(self):
		new_card = self.get_next_card()
		self.dealer_cards.append(new_card)
		self.dealer_number += new_card
		if self.dealer_number.busted():
			self.dealer_busted = True
			print(new_card, 'dealer busted')


	def player_move(self):

		self.import_strategy()

		while self.current_hand < self.hand_number:

			while True:

				strat = self.lookup_strategy(self.current_hand)

				self.print_current_hand(self.current_hand)
				print("Choosen strategy is :", strat)

				if strat == 'S':
					break


				elif strat == 'H':
					if self.player_hit(self.current_hand):
						pass
					else:
						break


				elif strat == 'D':
					self.bet *= 2 
					self.player_hit(self.current_hand)
					break


				elif strat == 'P':

					# add a empty hand as second hand
					self.player_cards.append([None])

					# give the second card to a new hand 
					first_hand = self.player_cards[self.current_hand]
					second_hand = self.player_cards[-1]
					second_hand[0] = first_hand[1]
					first_hand.remove(first_hand[1])

					self.player_busted.append(False)

					self.player_number.append(None)
					# recalculate current hand's number value
					self.player_number[self.current_hand] = number(first_hand[0])
					# the split hand's value
					self.player_number[-1] = number(second_hand[0])

					# get a new second card for current hand
					self.player_hit(self.current_hand)
					# get a new second card for the new hand
					self.player_hit(self.hand_number)

					self.hand_number +=1

			
			self.current_hand +=1

	def dealer_move(self):
		while not self.dealer_number.soft_17():
			self.dealer_hit()

	def get_next_card(self):
		if self.card_source == "random":
			values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
			suits = ['H','S','D','C']
			return card(random.choice(values),random.choice(suits))
		elif card_source == "deck":
			pass


	# import the stored strategy and store them in:
	# self.stg: general strategy
	# self.stp: pair strategy
	# self.sts: soft strategy
	def import_strategy(self):
		path_general = 'strategy/strat_general.csv'
		path_pair = 'strategy/strat_pair.csv'
		path_soft = 'strategy/strat_soft.csv'
		self.stg = pd.read_csv(path_general,sep = ' ').set_index('H')
		self.stp = pd.read_csv(path_pair,sep = ' ').set_index('H')
		self.sts = pd.read_csv(path_soft,sep = ' ').set_index('H')
		self.stg.index = self.stg.index.map(str)
		self.stp.index = self.stp.index.map(str)
		self.sts.index = self.sts.index.map(str)

	# look up the strategy based on the player_cards and dealer_cards[0]
	def lookup_strategy(self, hand_number):

		dealer_card = self.dealer_cards[0]
		ret = None
		if len(self.player_cards[hand_number]) == 2:
			first_card = self.player_cards[hand_number][0]
			second_card = self.player_cards[hand_number][1]
			if first_card.get_value() == second_card.get_value():
				index = first_card.get_value()+','+first_card.get_value()
				if index in self.stp.index:
					return self.stp[dealer_card.get_value()][index]
		
		print(self.player_number[hand_number])
		if self.player_number[hand_number].is_soft:
			# This means it's a split Ace, no more actions
			if self.player_cards[hand_number][0].get_value() == 'A' and self.hand_number > 1:
				return 'S'

			index = str(self.player_number[hand_number].val())
			ret = self.sts[dealer_card.get_value()][index]

		else:
			index = str(self.player_number[hand_number].val())
			ret = self.stg[dealer_card.get_value()][index]

		if len(self.player_cards[hand_number]) > 2 and ret == 'D':
			ret = 'H'

		return ret


	def print_current_hand(self, hand_number):
		print("player cards: ", self.player_cards[hand_number])
		print("dealer cards: ", self.dealer_cards)
		



if __name__ == "__main__":
	i = 0
	final = 0
	while True:
		i +=1 
		p = play(10)
		res = p.play()
		print(res)
		final += res
		print(i,final)
	