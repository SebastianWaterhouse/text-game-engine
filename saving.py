import os, json, main

availsaves = os.walk("saves")

def loadsave(target):
	return(json.loads(open("saves/" + target + ".json").read()))

def unpacksave(save):
	x = save["entitites"]["player"]["health"]
	z = {"health":x}
	return(z)

def createsavedata(playerloc):
	y = {
		"version":main.version,
		"entitities":{
			"player":{
				"health":main.playerloc.health
			}
		}
	}
	return(y)

def save(data, slot):
	dire = "saves" + slot + ".json"
	json.dump(data, dire)