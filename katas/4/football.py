#!/usr/bin/python

file = open("football.dat", "r")

line = file.readline()

lowscore = -1

while (line != ""):
	strs = line.split()
	if (len(strs) > 5):
		if(strs[0] != "Team"):
			curscore = abs(int(strs[6]) - int(strs[8]))
			if (lowscore < 0): 
				lowscore = curscore
				team = strs[1]
			else:
				if (curscore < lowscore): 
					lowscore= curscore
					team = strs[1]
	line = file.readline()

print ("The team with the smallest difference is: " + team)
