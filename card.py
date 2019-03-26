
class card:
	'''
		self.value: an one character string in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
		self.suit: an one character string in ['H','S','D','C']
	'''

	def __init__(self, value: str, suit: str) -> None:
		self.value = value
		self.suit = suit
		

	# return a string in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
	def get_value(self) -> str:
		return self.value


	# return a string in ['H','S','D','C']
	def get_suit(self) -> str:
		return self.suit


	# return whether this card is a 'T','J','Q','K'
	def is_ten(self) -> bool:
		return True if self.get_number().val() == 10 else False


	# return whether this card is an 'A'
	def is_ace(self) -> bool:
		return True if self.value == 'A' else False


	def get_number(self):
		return number(self)


	def __str__(self) -> str:
		return self.get_value() + self.get_suit()

	def __repr__(self) -> str:
		return self.get_value() + self.get_suit()


class number:

	# initialize with one card
	# if this is a soft number, we record its lowest possible number value
	def __init__(self, c: card) -> None:
		self. m = {'A': 1, '2': 2, '3': 3, 
			'4': 4, '5': 5, '6': 6,
			'7': 7, '8': 8, '9': 9,
			'T': 10, 'J': 10, 'Q': 10,
			'K': 10}
		v = c.get_value()
		self.value = self.m[v]
		self.is_soft = False
		if v == 'A':
			self.is_soft = True


	# calculate the number after addding one card
	def __add__(self, c: card) -> card:
		v = c.get_value()
		value = self.m[v]
		if self.is_soft:
			self.value += value
			if self.value > 11:
				self.is_soft = False
		else:
			self.value += value
			if v == 'A' and self.value <=11:
				self.is_soft = True

		return self


	def __gt__(self, n) -> bool:
		val1 = self.value
		if self.is_soft:
			val1 += 10
		val2 = n.value
		if n.is_soft:
			val2 += 10
		return val1 > val2

	def __lt__(self, n) -> bool:
		return not self.__ge__(n)

	def __eq__(self, n) -> bool:
		val1 = self.value
		if self.is_soft:
			val1 += 10
		val2 = n.value
		if n.is_soft:
			val2 += 10
		return val1 == val2

	def soft_17(self) -> bool:
		if self.is_soft and self.value > 17:
			return True
		if not self.is_soft and self.value >= 17:
			return True
		return False


	# return the numerical value of the number
	def val(self) -> int:
		return self.value


	# return whether this is a busted number
	def busted(self) -> bool:
		return self.value > 21


	def __str__(self) -> str:
		if self.is_soft:
			return str(self.val()) + "soft"
		else:
			return str(self.val()) + "hard"

	def __repr__(self) -> str:
		if self.is_soft:
			return str(self.val()) + "soft"
		else:
			return str(self.val()) + "hard"

if __name__ == "__main__":
	pass
	# c1 = card('2','S')
	# c2 = card('A','C')
	# c3 = card('4','C')

	# print(c1.get_number())

	# v = number(c1)
	# print(v)
	# v += c2
	# print(v)
	# v += c3
	# print(v)


	
