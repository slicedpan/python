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
	
def chop(theNum, theList):
	print "-----------------------------------------------------"
	counter = 0
	while(1):
	
		
		
		print "List: " + str(theList)
		length = len(theList)
		print "Length: " + str(length)	
		
		if (length == 0): return -1
		
		mid = length // 2
		print "midpoint: " + str(mid) + " = " + str(theList[mid])
		
		if (theList[mid] == theNum): return mid + counter
		
		if (theNum > theList[mid]): 
			i = 0
			while (i <= mid):
				del(theList[0])
				counter += 1
				i += 1
		else:
			i = mid
			while (i < length):
				del(theList[mid])
				i += 1
 
test_chop()
print chop(23, [1,3,6,8,9,13,16,19,23,25,29,35,50,61])
				
				