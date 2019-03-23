class card:
	'''
		self.value: an one character string in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
		self.suit: an one character string in ['H','S','D','C']
	'''
	def __init__(self, value: str, suit: str):
		self.value = value
		self.suit = suit
		
	def get_value(self):
		return self.value

	def get_suit(self):
		return self.suit

	def is_ten(self):
		if self.get_number_value() == 10:
			return True
		else:
			return False

	def is_ace(self):
		if self.value == 'A':
			return True
		else:
			return False

	def get_number_value(self):
		m = {'A': [1,11], '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 10,'Q': 10,'K': 10}
		return m[self.value]

	def __str__(self):
		return self.get_value()+self.get_suit()

if __name__ == "__main__":
	pass
	c = card('A','C')
	print(c.get_number_value())
	#values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
	#suits = ['H','S','D','C']
	#one_deck = [card(value,suit) for value in values for suit in suits]
	#eightdeck = one_deck * 8
	#for i in range(len(eightdeck)):
	#	print(eightdeck[i])
	#a = [card('A','S')]
	#b = a*2
	
