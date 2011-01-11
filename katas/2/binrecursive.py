#!/usr/bin/python

mystr = "Hello World!"





def binarySearch(theList, theNum):

	length = len(theList)
	print "list: " + str(theList)
	print "length: " + str(length)

	
	if (length == 0):
		return -1

	mid  = length // 2
	
	print "checking pos: " + str(mid) + " = " + str(theList[mid])
	
	if (theList[mid] == theNum):
		return mid
	
	if (theList[mid] > theNum):
		return binarySearch(theList[:mid], theNum)
		
	retnum = binarySearch(theList[mid + 1 :], theNum)
	if (retnum == -1): return -1
	return retnum + mid + 1
		
	
def chop (num, list):
	return binarySearch(list,num)
	
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

test_chop()




	
