import sys

def exit0():
	print("Exited with code 0")
	sys.exit()

def optionshelp():
	print("This is an engine for a text-based game. There is very little included with it by default. Search out additional packages for actual content.")
	print("")
	print("Options:")
	print("-v : verbose mode (semi-implemented)")
	print("-(?/h/help/man/manual) : help")
	sys.exit()

def dictreverse(origin):
	return({x:y for x,y in origin.items()})

class health:
	def __init__(self, maxh):
		self.maxh = maxh
		self.current = maxh
	def death(self):
		print("You died.")
		exit0()
	def hurt(self, amt):
		newh = self.current - amt
		print("You were damaged by " + str(amt) + " hitpoints. You are on " + str(newh) + ".")
		if newh > 0:
			self.current = newh
		else:
			self.death()
	def heal(self, amt):
		newh = self.current + amt
		if newh > 100:
			self.current = 100
			diff = 100 - self.current
			print("You were healed by " + str(diff) + " hitpoints. You are on 100.")
		else:
			self.current = self.current + amt
			print("You were healed by " + str(amt) + " hitpoints. You are on " + str(newh) + ".")
	def printhealth(self):
		print("You are currently on " + str(self.current) + " hitpoints.")