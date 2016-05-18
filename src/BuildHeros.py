from Hero import *
class Heros:
	def __init__(self):
		self.heros = []
		self.heros.append(Hero(cname='曹操', name='caocao', country='wei', sex=1, baseHP=4, ident=1))
		self.heros.append(Hero(cname='司马懿', name='simayi', country='wei', sex=1, baseHP=3, ident=2))
		self.heros.append(Hero(cname='夏侯惇', name='xiahoudun', country='wei', sex=1, baseHP=4, ident=3))
		self.heros.append(Hero(cname='张辽', name='zhangliao', country='wei', sex=1, baseHP=4, ident=4))
		self.heros.append(Hero(cname='许褚', name='xuchu', country='wei', sex=1, baseHP=4, ident=5))
		self.heros.append(Hero(cname='郭嘉', name='guojia', country='wei', sex=1, baseHP=3, ident=6))
		self.heros.append(Hero(cname='甄姬', name='zhenji', country='wei', sex=0, baseHP=3, ident=7))
		self.heros.append(Hero(cname='刘备', name='liubei', country='shu', sex=1, baseHP=4, ident=8))
		self.heros.append(Hero(cname='关羽', name='guanyu', country='shu', sex=1, baseHP=4, ident=9))
		self.heros.append(Hero(cname='张飞', name='zhangfei', country='shu', sex=1, baseHP=4, ident=10))
		self.heros.append(Hero(cname='诸葛亮', name='zhugeliang', country='shu', sex=1, baseHP=3, ident=11))
		self.heros.append(Hero(cname='赵云', name='zhaoyun', country='shu', sex=1, baseHP=4, ident=12))
		self.heros.append(Hero(cname='马超', name='machao', country='shu', sex=1, baseHP=4, ident=13))
		self.heros.append(Hero(cname='黄月英', name='huangyueying', country='shu', sex=0, baseHP=3, ident=14))
		self.heros.append(Hero(cname='孙权', name='sunquan', country='wu', sex=1, baseHP=4, ident=15))
		self.heros.append(Hero(cname='甘宁', name='ganning', country='wu', sex=1, baseHP=4, ident=16))
		self.heros.append(Hero(cname='吕蒙', name='lvmeng', country='wu', sex=1, baseHP=4, ident=17))
		self.heros.append(Hero(cname='黄盖', name='huanggai', country='wu', sex=1, baseHP=4, ident=18))
		self.heros.append(Hero(cname='周瑜', name='zhouyu', country='wu', sex=1, baseHP=3, ident=19))
		self.heros.append(Hero(cname='大乔', name='daqiao', country='wu', sex=0, baseHP=3, ident=20))
		self.heros.append(Hero(cname='陆逊', name='luxun', country='wu', sex=1, baseHP=3, ident=21))
		self.heros.append(Hero(cname='孙尚香', name='sunshangxiang', country='wu', sex=0, baseHP=3, ident=22))
		self.heros.append(Hero(cname='华佗', name='huatuo', country='qun', sex=1, baseHP=3, ident=23))
		self.heros.append(Hero(cname='吕布', name='lvbu', country='qun', sex=1, baseHP=4, ident=24))
		self.heros.append(Hero(cname='貂蝉', name='diaochan', country='qun', sex=0, baseHP=3, ident=25))

bHeros = Heros().heros