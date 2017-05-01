import funcs, loader
import json, sys

verbose = 0

if sys.argv[-1] == "-v":
	verbose = 1
except:
	pass

default_package = "defualt"

loader.loaded_packages=[default_package]

loader.packaged(loader.packagesl, verbose)

if len(sys.argv) != 0:
	for n in sys.argv:
		loader.loaded_packages.append(n)
else:
	appendpackages(loader.loaded_packages, verbose)

json_chooser(loader.loaded_packages, verbose)

branchesj = json.loads(open("data/" + loader.branchej + "/branches.json"))

cat_aggregator()

sbranch = "a0"

while True:
	branch = branchesj[sbranch]
	print(branch["begin"])
	if branch["run"] != "null":
		eval(branch["run"])
	respons = input("")
	respons = respons.lower()
	for retype in catsj["categories"]:
		if respons in catsj["categories"][retype]:
			respons = retype
	if respons in branch["responses"]:
		sbranch = branchesj[sbranch]["responses"][respons]
	else:
		sbranch = branchesj[sbranch]["loop"]