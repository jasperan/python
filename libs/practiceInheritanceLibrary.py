class Person2(object):
	def __init__(self, numberOfLegs, numberOfArms):
		self.numberOfArms = numberOfArms
		self.numberOfLegs = numberOfLegs
	def functionProblem(self):
		print 'I am a person'
class LivingOrganism2(object):
	def __init__(self, aliveState):
		self.aliveState = aliveState
	def functionProblem(self):
		print 'I am a living organism'