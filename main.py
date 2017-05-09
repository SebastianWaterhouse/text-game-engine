import funcs, loader
import json, sys

verbose = 0
helpsyms = ["-h", "-help", "-man", "-manual", "-?"]

args = sys.argv
args.remove("main.py")

if len(args) != 0:
	if args[0] in helpsyms:
		funcs.optionshelp()
	elif "-v" in args:
		verbose = 1
		args.remove("-v")
	else:
		print("Use -? for more information on the command line options available.")
		sys.exit()

loader.packaged(loader.packagesl, verbose)

loaded_packages = loader.appendpackages(verbose)

branchej = loader.json_chooser(loaded_packages, verbose)

branchej = loader.packagest[branchej]

branchesj = json.loads(open("data/" + branchej + "/branches.json").read())

catsj = loader.cat_aggregator(loader.sel_cats, verbose)

sbranch = "a0"

while True:
	try:
		branch = branchesj[sbranch]
		print(branch["begin"])
		if branch["run"] != "null":
			eval(branch["run"])
		respons = input("")
		respons = respons.lower()
		for retype in catsj:
			if respons in catsj[retype]:
				respons = retype
		if respons in branch["responses"]:
			sbranch = branchesj[sbranch]["responses"][respons]
		else:
			sbranch = branchesj[sbranch]["loop"]
	except Exception:
		if verbose == 1:
			print("Exception raised because verbose is on.")
			raise
		else:
			print("WARNING: Error occurred. Continuing.")