import time
'''
	TimeAttack class
	Singleton who have loop to check the checkpoints
'''
class TimeAttack:
	_instance = None
	
	''' Initialization of the instance'''
	def __init__(self, agent):
		self.getInstance(agent)

	''' Return the instance if already exist, if not create an instance as a singleton '''
	@classmethod
	def getInstance(cls, agent):
		if cls._instance is None:
			cls.agent = agent
			cls._instance = 1

		return cls._instance

	''' To check each player's checkpoint and update them'''
	def triggerCheckpoint(self):
		# Check each players
		players = self.agent.range
		for playerID in players:
			player = players[playerID]

			# Check each checkpoints
			checkpoints = self.agent.game['dtFire']
			id = 0
			for cp in checkpoints:
				id = id + 1

				# If the player is in the range of the checkpoint
				if player['x'] <= cp['x'] + 2 and player['x'] >= cp['x'] - 2:
					if player['y'] <= cp['y'] + 2 and player['y'] >= cp['y'] - 2:

						# If the player validate the previous checkpoint
						if player['life'] == id - 1:
							player['life'] = id

						# If the id is the finish and the player validate the last checkpoint
						if id == 0 and player['life'] == checkpoints[len(checkpoints)]:
							# save score
							player['life'] = 0

	''' Loop during the time attack time'''
	def run(self):
		print('run')
		for i in range(0, 10000):
			self.triggerCheckpoint()
			time.sleep(0.1)
		return 0
