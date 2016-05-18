from BuildCards import *
from random import *
import copy

class Deck:
	def __init__(self):
		self.cardnum = 104
		self.cardlist = copy.deepcopy(Cards().cards)
		self.discardlist = []
		self.shuffle()

	def shuffle(self):
		for i in range(1000):
			j = randint(0, self.cardnum-1)
			k = randint(0, self.cardnum-1)
			temp = self.cardlist[j]
			self.cardlist[j] = self.cardlist[k]
			self.cardlist[k] = temp

	def draw(self, num):
		outStr = ""
		for i in range(num):
			outStr = outStr + "," + str(self.cardlist[0].ident)
			self.discardlist.append(self.cardlist[0])
			del self.cardlist[0]
		self.cardnum -= num
		if self.cardnum == 0:
			self.cardlist = copy.copy(self.discardlist)
			self.discardlist = []
			self.shuffle()
			self.cardnum = len(self.cardlist)
		return outStr

	def newCardlist(self):
		self.cardlist = self.discardlist
		self.discardlist = []
		self.shuffle()



