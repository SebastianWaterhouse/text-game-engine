import sys

def exit0():
	print("Exited with code 0")
	sys.exit()

def optionshelp():
	print("This is an engine for a text-based game. There is very little included with it by default. Search out additional packages for actual content.")
	print("")
	print("Options:")
	print("-v : verbose mode")
	print("-(?/h/help/man/manual) : help")
	sys.exit()

def dictreverse(origin):
	return({x:y for x,y in origin.items()})