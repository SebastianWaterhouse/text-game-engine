import funcs, loader, saving, entities
import json, sys

verbose = 0
helpsyms = ["-h", "-help", "-man", "-manual", "-?"]
version = "0.06"

f = True

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

while f == True:
	print("Would you like to load a save?")
	s = input("Y/N: ")
	s = s.lower()
	if s == "y":
		if len(saving.availsaves) == 0:
			print("No saves available to load. Starting new game.")
			toloadsave = "default"
		else:
			print("What save would you like to load? These are the saves available: " + str(saving.availsaves))
			toloadsave = saving.toload(verbose)
		f = False
	elif s == "n":
		print("Starting new game.")
		toloadsave = "default"
		f = False
	else:
		print("This is a yes or no question.")

loadedsave = saving.loadsave(toloadsave)
savedata = saving.unpacksave(loadedsave)

print(savedata)

loader.packaged(loader.packagesl, verbose)
if savedata["branchf"] == "null":
	loaded_packages = loader.appendpackages(verbose)
	branchej = loader.json_chooser(loaded_packages, verbose)
else:
	branchej = savedata["branchf"]
branchej = loader.packagest[branchej]
branchesj = json.loads(open("data/" + branchej + "/branches.json").read())
catsj = loader.cat_aggregator(loader.sel_cats, verbose)

sbranch = savedata["branch"]

player = entities.entity(int(savedata["health"]))

while True:
	try:
		branch = branchesj[sbranch]
		print(branch["begin"])
		if branch["run"] != "null":
			eval(branch["run"])
		respons = input("")
		respons = respons.lower()
		if respons == "save":
			s = saving.tosave()
			d = saving.createsavedata(version, player.health.current, sbranch, branchej)
			saving.save(d, s)
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