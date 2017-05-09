import os, json

packagesl = next(os.walk("data"))[1]
packagesl.remove("__pycache__")
packagesd = {}
packagest = {}
sel_cats = []
sel_packagesj = []
packnrev = {}

def dictreverse(origin):
	return({x:y for x,y in origin.items()})

def packaged(sel_packages, verbose):
	for pack in sel_packages:
		typee = json.loads(open("data/" + pack + "/desc.json").read())["type"]
		packn = json.loads(open("data/" + pack + "/desc.json").read())["name"]
		d = {packn:typee}
		e = {packn:pack}
		packagesd.update(d)
		packagest.update(e)

def json_chooser(sel_packages, verbose):
	for packip in sel_packages:
		print(packip)
		print(packagesd[packip])
		if packagesd[packip] in ["dual", "branches"]:
			if verbose == 1: print("package loaded with branches")
			sel_packagesj.append(packip)
		if packagesd[packip] in ["dual", "cats"]:
			if verbose == 1: print("package loaded with cats")
			sel_cats.append(packip)
	if len(sel_packagesj) != 1:
		if verbose == 1: print("branchej set to last pack. loaded")
		return(sel_packagesj[-1])
	else:
		if verbose == 1: print("branchej set to sole pack. loaded")
		return(sel_packagesj[0])

def cat_aggregator(sel_cats, verbose):
	cats = {}
	for packy in sel_cats:
		cats.update(json.loads(open("data/" + packagest[packy] + "/cats.json").read())["categories"])
	return(cats)

def appendpackages(verbose):
	loaded_packages = ["default"]
	go = 1
	while go == 1:
		print("You will load the default package. Is this OK? Y/N")
		pacselec = input("").lower()
		if pacselec == "n":
			print("The packages available to load are (in name:type form): " + str(packagesd))
			resp = input("Type the name of each package you want to load separated by a comma (no spaces between items). Leave blank to just load the defualt package. ")
			print(resp.split(","))
			loaded_packages.extend(resp.split(","))
			print(loaded_packages)
			go = 0
		elif pacselec == "y":
			print("Loading default package")
			go = 0
		else:
			print("This is a yes or no question.")
	return(loaded_packages)