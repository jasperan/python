import sys
sys.path.append('./libs/')

from practiceInheritanceLibrary import Person2
from practiceInheritanceLibrary import LivingOrganism2

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
