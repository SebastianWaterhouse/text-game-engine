import os, json

packagesl = next(os.walk("data"))[1]
packagesd = {}
loaded_branchej = ""
sel_cats = []
cats = {}
sel_packagesj = []
loaded_packages = []

def packaged(sel_packages, verbose):
	for pack in sel_packages:
		typee = json.loads(open("data/" + pack + "/desc.json")).read()["type"]
		packn = json.loads(open("data/" + pack + "/desc.json")).read()["name"]
		d = {packn:typee}
		packagesd.update(d)

def json_chooser(sel_packages, verbose):
	for pack in sel_packages:
		if packagesd[pack] in ["dual", "branches"]:
			if verbose == 1: print("package loaded with branches")
			sel_packagesj.append(pack)
		if packagesd[pack] in ["dual", "cats"]:
			if verbose == 1: print("package loaded with cats")
			sel_cats.append(pack)
	if len(sel_packagesj) != 1:
		if verbose == 1: print("loaded_branchej set to last pack. loaded")
		loaded_branchej = sel_packagesj[-1]

def cat_aggregator(sel_cats, verbose):
	pass

def appendpackages(loaded_packagess, verbose):
	while go == 1:
		print("You will load the default package. Is this OK? Y/N")
		pacselec = input("").lower()
		if pacselec == "y":
			print("The packages available to load are (name:type): " + packagesd)
			resp = input("Type the name of each package you want to load separated by a space. Leave blank to just load the defualt package. ")
			for a in resp:
				loaded_packagess.append(a)
			go = 0
		elif pacselec == "n":
			print("Loading default package")
			go = 0
		else:
			print("This is a yes or no question.")