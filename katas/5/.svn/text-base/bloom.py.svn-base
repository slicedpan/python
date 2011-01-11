#!/usr/bin/python
import hashlib
import random

def randomletters(numletters):
	str = ""
	n = 0
	while (n < numletters):
		str += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
		n += 1
	return str

class bloomfilter:
	def __init__(self, maxhashes):
		self.bitset = 0
		self.numhashes = maxhashes
		self.counter = 0
		n = 0
		while(n < maxhashes):
			self.bitset = 0
			n += 1
		print self.bitset
		self.salt = []
		n = 0
		print "generating salts:"
		while(n < maxhashes):
			self.salt.append(randomletters(10))
			n += 1
		print "done"
		print self.salt
		
	def add(self, instr):
		n = 0
		self.counter += 1
		if (self.counter == 2000): 
			print instr
			self.counter = 0
		while (n < self.numhashes):
			self.bitset = self.bitset | int(hashlib.md5(instr).hexdigest(), 16)
			n += 1
	def out(self):
		print self.bitset
	def check(self, chstr):
		n = 0
		while (n < self.numhashes):
			print "checking"
			if (self.bitset == self.bitset | int(hashlib.md5(chstr).hexdigest(), 16)): return True
			n += 1
		return False
	
random.seed("this is the seed")

file = open(r'\\SAMBA-SERVER\RootDir\usr\share\dict\words', "r")
#file = open(r'wordlist', "r")

bf = bloomfilter(100)

line = file.readline()
print "Hashing dictionary:"
while (line != ""):
	#print "Hashing: " + line
	bf.add(line.strip())
	line = file.readline()
	
print "Hashed."
bf.out()

running = True

while (running == True):
	word = raw_input("Enter a word to Check: ")
	if (bf.check(word) == True):
		print "That word is in the dictionary"
	else:
		print "That word is not in the dictionary"
	if (word == "quit"):
		running = False		

	

