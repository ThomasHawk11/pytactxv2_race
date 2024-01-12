import time


class GameLoop:
	_instance = None

	def __init__(self, agent):
		self.getInstance(agent)

	@classmethod
	def getInstance(cls, agent):
		if cls._instance is None:
			print('new instance')
			cls.etat = 0
			cls.agent = agent
			cls._instance = 1
		return cls._instance

	def next(self):
		self.etat = self.etat + 1
		if self.etat == 4:
			self.etat = 0
		self.action()

	def getEtat(self):
		return self.etat

	def getEtatAsString(self):
		match self.etat:
			case 0 :
				return "init"
			case 1 :
				return "warm up"
			case 2 :
				return "time attack"
			case 3 :
				return "scores"
				
	def action(self):
		match self.etat:
			case 0 :
				self.init()
			case 1 :
				self.warmup()
			case 2 :
				self.timeAttack()
			case 3 :
				self.scores()

	def init(self):
		self.agent.ruleArena("info", "Initialisation du jeu")
		return 0

	def warmup(self):
		self.agent.ruleArena("info", "Warm Up : (time)")
		return 0
		
	def timeAttack(self):
		self.agent.ruleArena("info", "Initialisation du Time Attack")
		time.sleep(2)
		self.agent.ruleArena("info", "Time Attack : (time)")
		return 0
			
	def scores(self):
		self.agent.ruleArena("info", "Fin de jeu ! (scores)")
		return 0