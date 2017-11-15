from connector import connector
from webScrapper import webScrapper

class Information(object):
	desc = ""
	category = ""
	apps = ""

ifname = raw_input('Enter input filename : ')
ofname = raw_input('Enter output filename : ')

#To save overhead in the same run
info = {}

#Object for handling database
db = connector()

#open file for writing
output = open(ofname,'w')

#Reading file line by line
with open(ifname) as f:
	for line in f:
		line = line.strip()
		if not line:
			continue
		#line is now extension
		#First check in dictionary,then database if it has the entry or not
		if line in info:
			desc = info[line].desc
			category = info[line].category
			apps = info[line].apps
		else:
			op = db.search(line)
			tmp = Information()
			if (op is not None):
				desc = op[1]
				category = op[2]
				apps = op[3]
				#Store it in dictionary
				tmp.category = category
				tmp.desc = desc
				tmp.apps = apps
				info[line] = tmp
			else:
				#Search for it on the web
				web = webScrapper(line) 
				#Store it in database
				desc = web.shortDescription()
				category = web.fileType()
				apps = web.associatedApplications()
				#Store it in dictionary
				tmp.category = category
				tmp.desc = desc
				tmp.apps = apps
				info[line] = tmp			
				db.insert(line,desc,category,apps)

		output.write(line+'\n')
		output.write('Description : ' + desc)
		output.write('\n')
		output.write('Category : ' + category)
		output.write('\n')
		output.write('Associated Applications : ' + apps)
	 	output.write("\n\n")
