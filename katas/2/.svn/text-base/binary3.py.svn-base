#!/usr/bin/python

def test_chop():
	assert(-1 == chop(3, []))
	assert(-1 == chop(3, [1]))
	assert(0 == chop(1, [1]))
	#
	assert(0 ==  chop(1, [1, 3, 5]))
	assert(1 ==  chop(3, [1, 3, 5]))
	assert(2 ==  chop(5, [1, 3, 5]))
	assert(-1 == chop(0, [1, 3, 5]))
	assert(-1 == chop(2, [1, 3, 5]))
	assert(-1 == chop(4, [1, 3, 5]))
	assert(-1 == chop(6, [1, 3, 5]))
	#
	assert(0 == chop(1, [1, 3, 5, 7]))
	assert(1 ==  chop(3, [1, 3, 5, 7]))
	assert(2 == chop(5, [1, 3, 5, 7]))
	assert(3 == chop(7, [1, 3, 5, 7]))
	assert(-1 == chop(0, [1, 3, 5, 7]))
	assert(-1 == chop(2, [1, 3, 5, 7]))
	assert(-1 == chop(4, [1, 3, 5, 7]))
	assert(-1 == chop(6, [1, 3, 5, 7]))
	assert(-1 == chop(8, [1, 3, 5, 7]))	
	print "test passed!"
	
class binarylist:
	def __init__(self, theList, offset):
		self.m_list = theList
		if (len(self.m_list) != 0):
			print "------------------------------------"
			print "List: " + str(theList)
			self.midpos = len(theList) // 2
			print "midpos: " + str(self.midpos)
			self.value = theList[self.midpos]
			print "value: " + str(self.value)
			self.offset = offset
			if (len(theList) > 1):
				self.upperlist = binarylist(theList[self.midpos + 1:], self.midpos + 1)
				self.lowerlist = binarylist(theList[:self.midpos],0)
	def getpos(self, theNum):
		if (len(self.m_list) == 0): return -1
		if (theNum == self.value): return self.midpos + self.offset
		if (len(self.m_list) == 1): return -1
		if (theNum < self.value): return self.lowerlist.getpos(theNum)
		return self.upperlist.getpos(theNum)
		
def chop(theNum, theList):
	list1 = binarylist(theList,0)
	return list1.getpos(theNum)
	
test_chop()


		
	
	