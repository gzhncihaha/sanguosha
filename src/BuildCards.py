import copy
from Card import *
class Cards:
	def __init__(self):
		self.cards = []
		self.cards.append(Card(suit="spade", number="7", name="slash", ident=1, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="spade", number="8", name="slash", ident=2, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="spade", number="8", name="slash", ident=3, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="spade", number="9", name="slash", ident=4, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="spade", number="9", name="slash", ident=5, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="spade", number="10", name="slash", ident=6, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="spade", number="10", name="slash", ident=7, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="2", name="slash", ident=8, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="3", name="slash", ident=9, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="4", name="slash", ident=10, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="5", name="slash", ident=11, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="6", name="slash", ident=12, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="7", name="slash", ident=13, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="8", name="slash", ident=14, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="8", name="slash", ident=15, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="9", name="slash", ident=16, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="9", name="slash", ident=17, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="10", name="slash", ident=18, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="10", name="slash", ident=19, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="J", name="slash", ident=20, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="club", number="J", name="slash", ident=21, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="heart", number="10", name="slash", ident=22, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="heart", number="10", name="slash", ident=23, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="heart", number="J", name="slash", ident=24, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="diamond", number="6", name="slash", ident=25, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="diamond", number="7", name="slash", ident=26, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="diamond", number="8", name="slash", ident=27, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="diamond", number="9", name="slash", ident=28, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="diamond", number="10", name="slash", ident=29, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="diamond", number="K", name="slash", ident=30, basetype="base", subtype="attack"))
		self.cards.append(Card(suit="heart", number="2", name="jink", ident=31, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="heart", number="2", name="jink", ident=32, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="heart", number="K", name="jink", ident=33, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="2", name="jink", ident=34, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="2", name="jink", ident=35, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="3", name="jink", ident=36, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="4", name="jink", ident=37, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="5", name="jink", ident=38, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="6", name="jink", ident=39, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="7", name="jink", ident=40, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="8", name="jink", ident=41, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="9", name="jink", ident=42, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="10", name="jink", ident=43, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="J", name="jink", ident=44, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="diamond", number="J", name="jink", ident=45, basetype="base", subtype="defend"))
		self.cards.append(Card(suit="heart", number="3", name="peach", ident=46, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="heart", number="4", name="peach", ident=47, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="heart", number="6", name="peach", ident=48, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="heart", number="7", name="peach", ident=49, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="heart", number="8", name="peach", ident=50, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="heart", number="9", name="peach", ident=51, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="heart", number="Q", name="peach", ident=52, basetype="base", subtype="recover"))
		self.cards.append(Card(suit="diamond", number="Q", name="peach", ident=53, basetype="base", subtype="recover"))

		self.cards.append(Card(suit="club", number="A", name="crossbow", ident=54, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="diamond", number="A", name="crossbow", ident=55, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="spade", number="2", name="double_sword", ident=56, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="spade", number="6", name="qinggang_sword", ident=57, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="spade", number="5", name="blade", ident=58, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="spade", number="Q", name="spear", ident=59, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="diamond", number="5", name="axe", ident=60, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="diamond", number="Q", name="halberd", ident=61, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="heart", number="5", name="kylin_bow", ident=62, basetype="equip", subtype="weapon"))
		self.cards.append(Card(suit="spade", number="2", name="eight_diagram", ident=63, basetype="equip", subtype="armor"))
		self.cards.append(Card(suit="club", number="2", name="eight_diagram", ident=64, basetype="equip", subtype="armor"))
		self.cards.append(Card(suit="spade", number="5", name="jueying", ident=65, basetype="equip", subtype="ghourse"))
		self.cards.append(Card(suit="club", number="5", name="dilu", ident=66, basetype="equip", subtype="ghourse"))
		self.cards.append(Card(suit="heart", number="K", name="zhuahuangfeidian", ident=67, basetype="equip", subtype="ghourse"))
		self.cards.append(Card(suit="heart", number="5", name="chitu", ident=68, basetype="equip", subtype="ahourse"))
		self.cards.append(Card(suit="spade", number="K", name="dayuan", ident=69, basetype="equip", subtype="ahourse"))
		self.cards.append(Card(suit="diamond", number="K", name="zixing", ident=70, basetype="equip", subtype="ahourse"))

		self.cards.append(Card(suit="heart", number="3", name="amazing_grace", ident=71, basetype="trick", subtype="global"))
		self.cards.append(Card(suit="heart", number="4", name="amazing_grace", ident=72, basetype="trick", subtype="global"))
		self.cards.append(Card(suit="heart", number="A", name="god_salvation", ident=73, basetype="trick", subtype="global"))
		self.cards.append(Card(suit="spade", number="7", name="savage_assault", ident=74, basetype="trick", subtype="range"))
		self.cards.append(Card(suit="spade", number="K", name="savage_assault", ident=75, basetype="trick", subtype="range"))
		self.cards.append(Card(suit="club", number="7", name="savage_assault", ident=76, basetype="trick", subtype="range"))
		self.cards.append(Card(suit="heart", number="A", name="archery_attack", ident=77, basetype="trick", subtype="range"))
		self.cards.append(Card(suit="spade", number="A", name="duel", ident=78, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="A", name="duel", ident=79, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="diamond", number="A", name="duel", ident=80, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="heart", number="7", name="ex_nihilo", ident=81, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="heart", number="8", name="ex_nihilo", ident=82, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="heart", number="9", name="ex_nihilo", ident=83, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="heart", number="J", name="ex_nihilo", ident=84, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="3", name="snatch", ident=85, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="4", name="snatch", ident=86, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="J", name="snatch", ident=87, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="diamond", number="3", name="snatch", ident=88, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="diamond", number="4", name="snatch", ident=89, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="3", name="dismantlement", ident=90, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="4", name="dismantlement", ident=91, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="Q", name="dismantlement", ident=92, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="3", name="dismantlement", ident=93, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="4", name="dismantlement", ident=94, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="heart", number="Q", name="dismantlement", ident=95, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="Q", name="collateral", ident=96, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="K", name="collateral", ident=97, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="J", name="nullification", ident=98, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="Q", name="nullification", ident=99, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="club", number="K", name="nullification", ident=100, basetype="trick", subtype="single"))
		self.cards.append(Card(suit="spade", number="6", name="indulgence", ident=101, basetype="trick", subtype="delay"))
		self.cards.append(Card(suit="club", number="6", name="indulgence", ident=102, basetype="trick", subtype="delay"))
		self.cards.append(Card(suit="heart", number="6", name="indulgence", ident=103, basetype="trick", subtype="delay"))
		self.cards.append(Card(suit="spade", number="A", name="lightning", ident=104, basetype="trick", subtype="delay"))

bCards = Cards().cards
iCard = [None for i in range(105)]
for card in bCards:
	iCard[card.ident] = copy.copy(card)
noTarget = ["jink", "peach", "amazing_grace", "god_salvation", "savage_assault", "archery_attack", "ex_nihilo", "nullification", "lightning"]

def getCardsTargetNum(s):
	i = int(s)
	card = iCard[i]
	if card.name in noTarget or card.basetype == "equip":
		return 0
	elif card.name == "collateral":
		return 2
	else:
		return 1

def getCardsIsImmediate(s):
	i = int(s)
	card = iCard[i]
	if card.basetype == "equip" or card.subtype == "delay" or card.subtype == "defend" or card.subtype == "recover":
		return True
	return False
