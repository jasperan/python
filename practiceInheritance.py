class Person(object):
	def __init__(self, numberOfLegs, numberOfArms):
		self.numberOfArms = numberOfArms
		self.numberOfLegs = numberOfLegs
	def functionProblem(self):
		print 'I am a person'
class LivingOrganism(object):
	def __init__(self, aliveState):
		self.aliveState = aliveState
	def functionProblem(self):
		print 'I am a living organism'
class Laura(Person, LivingOrganism):
	def __init__(self, age, course, aliveState, numberOfLegs, numberOfArms):
		self.age = age
		self.course = course
		#super(Laura, self).__init__(aliveState)
		super(Laura, self).__init__(numberOfLegs, numberOfArms)

var = Laura(22, 'Masters', 'Dead', 2, 2)
#print var.aliveState
print var.numberOfLegs
print var.numberOfArms
var.functionProblem()

# This is a problem.

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
class Laura2(object):
	def __init__(self, age, course, aliveState, numberOfLegs, numberOfArms):
		self.age = age
		self.course = course
		self.LivingOrganism2 = LivingOrganism2(aliveState)
		self.Person2 = Person2(numberOfLegs, numberOfArms)

var2 = Laura2(22, 'Masters', 'Dead', 2, 2)
print var2.LivingOrganism2.aliveState
print var2.Person2.numberOfLegs
print var2.Person2.numberOfArms
var2.Person2.functionProblem()
