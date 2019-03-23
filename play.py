from card import card
from deck import deck
import random

class play:
	'''
		self.dealer_cards: dealer cards, initialized to be 2, index 0 shown, index 1 hidden
		self.player_cards: player cards, initialized to be 2
		self.multiple_hands: boolean indicates if we have multiple hands to play
		self.player_number_value: player points (a number or "busted")
		self.dealer_number_value: dealer points (a number or "busted")
	'''
	@staticmethod
	def is_blackjack(card1: card, card2: card):
		if card1.is_ten() and card2.is_ace() or card1.is_ace and car2.is_ten():
			return True
		else:
			return False

	def __init__(self, bet, card_source = "random"):
		'''
			need to consider the situation when we need to split
			or just duplicate the result after one split??
		'''
		self.card_source = card_source
		self.dealer_cards = [self.get_next_card(),self.get_next_card()]
		self.player_cards = [self.get_next_card(),self.get_next_card()]
		self.multiple_hands = False
		self.bet = bet

	def play(self):


	def step_1(self):
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
		play_blackjack = is_blackjack(player_cards[0], player_cards[1])
		dealer_blackjack = is_blackjack(dealer_cards[0], dealer_blackjack[1])

		if play_blackjack and not dealer_blackjack:
			return [True, self.bet * 2.5]
		elif dealer_blackjack and not play_blackjack:
			return [False, 0]
		elif play_blackjack and dealer_blackjack:
			return [True, self.bet * 2]
		else:
			return False

	def step_2(self):



	def next_move():


	def get_next_card(self):
		if self.card_source == "random":
			values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
			suits = ['H','S','D','C']
			return card(random.choice(values),random.choice(suits))
		elif card_source == "deck":
			pass

	def import_strategy(self):
		pass

	def lookup_strategy(self):
		pass

if __name__ == "__main__":
	