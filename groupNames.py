import os

nameSearch = "Names of ALL group members:"
nSLen = len(nameSearch)

groups = []
names = []
goofs = []

count = 0

for file in os.listdir(os.getcwd()):
	name = file.split(".")[0][4:]
	if name not in names:
		names.append(name)
	count += 1
	#print file
	submission = open(file, "r")
	for line in submission:
		if (nameSearch in line):
			groupMems = line[nSLen:]
			if (groupMems not in groups) and (len(groupMems) < 100):
				groups.append(groupMems)
			break
	submission.close()
			
groupNames = open("groupNames.txt", "w")
for group in groups:
	groupNames.write(group)
groupNames.close()

nameNames = open("names.txt", "w")
for name in names:
	nameNames.write(name + "\n")
nameNames.close()

goofNames = open("goofed.txt", "w")
groupNames = open("groupNames.txt", "r")
for name in names:
	appendHuh = 1
	llLine = ""
	for line in groups:
		#nname = name.lower().split("\n")[0]
		lLine = line.lower()
		#print "name is " + name
		#print "line is " + lLine
		if name in lLine:
			print name
			appendHuh = 0
			break
	print appendHuh
	if appendHuh == 1:
		goofs.append(name)
for goof in goofs:
	goofNames.write(goof + "\n")
goofNames.close()

#print count
			
	