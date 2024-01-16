import time
import timeAttack

'''
	GameLoop class
	To save an state and execute function regarding to the state
'''
class GameLoop:
	_instance = None

	''' Initialization of the instance'''
	def __init__(self, agent):
		self.getInstance(agent)

	''' Return the instance if already exist, if not create an instance as a singleton '''
	@classmethod
	def getInstance(cls, agent):
		if cls._instance is None:
			print('new instance')
			
			cls.state = 0
			cls.agent = agent
			cls._instance = 1
			cls.timeAttackInstance = timeAttack.TimeAttack(agent)
			
		return cls._instance

	''' To switch state in the right order and execute a function '''
	def next(self):
		self.state = self.state + 1
		if self.state == 4:
			self.state = 0
		self.action()

	''' To get the state of the gameloop '''
	def getEtat(self):
		return self.state

	''' To get the state as a name for display '''
	def getEtatAsString(self):
		match self.state:
			case 0 :
				return "init"
			case 1 :
				return "warm up"
			case 2 :
				return "time attack"
			case 3 :
				return "scores"

	''' Execute the function link to the state '''
	def action(self):
		match self.state:
			case 0 :
				self.init()
			case 1 :
				self.warmup()
			case 2 :
				self.timeAttack()
			case 3 :
				self.scores()

	''' Init function, to init left few time to setup the game '''
	def init(self):
		self.agent.ruleArena("info", "Initialisation du jeu")
		time.sleep(2)
		return 0

	''' WarmUp function, the moment where players join '''
	def warmup(self):
		self.agent.ruleArena("info", "Warm Up : (time)")
		return 0

	''' Time Attack function, in game moment, contains loop to check the checkpoints '''
	def timeAttack(self):
		self.agent.ruleArena("info", "Time Attack : (time)")
		self.agent.update()
		
		self.timeAttackInstance.run()
		# self.timeAttackInstance.run()
		
		return 0

	''' Scores function, the end game, where we show the scores '''
	def scores(self):
		self.agent.ruleArena("info", "Fin de jeu ! (scores)")
		return 0