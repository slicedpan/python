#!/usr/bin/python

import hashlib
import random

class bloomfilter:
	def __init__(self, hashnum):
		self.bitset = []
		self.salt = []
		self.numhashes = hashnum
		self.counter = 0
		n = 0
		while (n < hashnum):
			self.bitset.append(0)
			self.salt.append(randomletters(15))
			n += 1
	def add(self, str):
		n = 0
		self.counter += 1
		if (self.counter == 1000):
			print str
			self.counter = 0
		while (n < self.numhashes):
			self.bitset[n] = self.bitset[n] | int(hashlib.md5(str + self.salt[n]).hexdigest(),16)
			n += 1
	def check(self, str):
		n = 0
		while (n < self.numhashes):
			if (self.bitset[n] | int(hashlib.md5(str + self.salt[n]).hexdigest(),16) != self.bitset[n]): return False
			n += 1
		return True
		
def randomletters(numletters):
	str = ""
	n = 0
	while (n < numletters):
		str += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
		n += 1
	return str

wordlist = ["one", "two", "three" ,"four"]



length = len(wordlist)
bf = bloomfilter(1000)

file = open(r'\\SAMBA-SERVER\RootDir\usr\share\dict\words', "r")

line = file.readline()


print "Hashing dictionary:"
while (line != ""):
	#print "Hashing: " + line
	bf.add(line.strip())
	line = file.readline()
	
running = True

while (running == True):
	word = raw_input("Enter a word to Check: ")
	if (bf.check(word) == True):
		print "That word is in the dictionary"
	else:
		print "That word is not in the dictionary"
	if (word == "quit"):
		running = False	
		
		
		
		