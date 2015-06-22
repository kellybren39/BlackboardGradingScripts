import os

#location of things in the csv file
gradeLoc = 8
graderLoc = 3
nameLoc = 6

graderGrades = {}
graders = []
names = []

file = open("grades.csv", "r")

#for file2 in os.listdir(os.getcwd()):
	#print file2

for line in file:
	print line
	gLine = line.split(",")
	#print gLine
	if gLine[graderLoc] not in graders:
		graders.append(gLine[graderLoc])
		graderGrades[gLine[graderLoc]] = gLine[graderLoc] + ", " + gLine[gradeLoc]
		names.append(gLine[nameLoc])
	else:
		if gLine[nameLoc] not in names:
			graderGrades[gLine[graderLoc]] = graderGrades.get(gLine[graderLoc]) + ", " + gLine[gradeLoc]
			names.append(gLine[nameLoc])
			
gBreakdown = open("gBreakdown.csv", "w")
keys = graderGrades.keys()
for key in keys:
	gBreakdown.write(graderGrades.get(key) + "\n")
file.close()
gBreakdown.close()
	