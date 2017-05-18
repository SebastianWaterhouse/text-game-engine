import os, json

availsaves = next(os.walk("saves"))[2]
availsaves.remove("default.json")

def loadsave(target):
	return(json.loads(open("saves/" + str(target) + ".json").read()))

def unpacksave(save):
	h = save["entities"]["player"]["health"]
	cb = save["branch"]
	bf = save["branchf"]
	v = save["version"]
	bf = json.loads(open("data/" + bf + "/desc.json").read())["name"]
	z = {"health":h, "branch":cb, "branchf":bf, "version":v}
	return(z)

def createsavedata(vers, playerh, cbranch, branchf):
	y = {
		"branchf":branchf,
		"version":vers,
		"branch":cbranch,
		"entities":{
			"player":{
				"health":playerh
			}
		}
	}
	return(y)

def save(data, slot):
	dire = "saves/" + str(slot) + ".json"
	with open(dire, "w") as direct:
		json.dump(data, direct)
		print("Saving to slot " + str(slot))

def tosave():
	c = []
	e = True
	while e == True:
		print("What slot would you like to save to? Must be a number: ")
		a = input("")
		try:
			a = int(a)
			for b in availsaves:
				c.append(b[0])
			print(c)
			if str(a) in c:
				print("Are you sure you would like to overwrite slot " + str(a) + "?")
				d = input("Y/N: ")
				d = d.lower()
				if d == "y":
					e = False
			else:
				e = False
		except ValueError:
			print("Not a number!")
	return(a)

def toload(verbose):
	c = []
	e = True
	while e == True:
		print("What slot would you like to load? Must be a number: ")
		a = input("")
		try:
			a = int(a)
			for b in availsaves:
				c.append(b[0])
			print(c)
			if str(a) in c:
				print("Loading save " + str(a) + "!")
				e = False
			else:
				print("That save is not available.")
		except ValueError:
			print("Not a number!")
	return(a)