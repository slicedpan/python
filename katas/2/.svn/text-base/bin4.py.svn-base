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
	begin = 0
	length = len(theList)
	if (length == 0): return -1
	end = length

	while(1):

		if(begin == end): return -1
		print "List: " + str(theList[begin:end])
		mid =  ((end - begin) // 2) + begin
		print "Position: " + str(mid) + " = " + str(theList[mid])
		if (theNum == theList[mid]): return mid
		if (theNum < theList[mid]):
			end = mid
		else:
			begin = mid + 1
		

test_chop()