import json, funcs

catsf = open("cats.json").read()
catsj = json.loads(catsf)
branchesf = open("branches.json").read()
branchesj = json.loads(branchesf)

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