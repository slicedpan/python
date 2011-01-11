#!/usr/bin/python
import re

def makesane(str1):
	str1 = re.sub(r'\D', "", str1)
	return int(str1)

file = open("weather.dat", "r")

line = file.readline()

numlist = []

while(line != ""):
	strs = line.split()
	if (len(strs) > 5):
		if (strs[0] != "Dy"):
			numlist.append(makesane(strs[1]) - makesane(strs[2]))
		
	line = file.readline()
	
n = 1	
lowvar = numlist[0]
lowday = 0
while (n < len(numlist)):
	if (numlist[n] < lowvar):
		lowvar = numlist[n]
		lowday = n
	n += 1
	
print "lowest temp range occurred on the " + str(lowday + 1) + "th day"

	
	
	