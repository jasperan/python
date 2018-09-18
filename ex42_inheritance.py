class Animal(object):
	pass
class Dog(Animal):
	def __init__(self, name):
		self.name = name
class Cat(Animal):
	def __init__(self, name):
		self.name = name
		self.hairs = None
	def setHairs(self, hairs):
		self.hairs = hairs 
class Person(object):
	def __init__(self,  name):
		self.name = name
		self.pet = None
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass



rover = Dog('Rover')
satan = Cat('Satan')
mary = Person('Mary')
mary.pet = satan
frank = Employee('Frank', 12000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()

print rover.name
print satan.name
print mary.name
print 'Mary\'s pet name %s and number of hairs: %s' % (mary.pet.name, mary.pet.hairs)
print 'Changing number of hairs to mary\'s pet to 500'
mary.pet.hairs = 500
print 'New number of hairs for pet %s: %s' % (mary.pet.name, mary.pet.hairs)

print 'Information about super with Employee - Person:'
print 'Frank is an employee.'
print 'Printing information about frank. Name: %s, Pet: %s, Salary: %s' % (frank.name, frank.pet.name, frank.salary)
print 'Frank\'s attribute is salary, and inherits name and pet from its superclass'

