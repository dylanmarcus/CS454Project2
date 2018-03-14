import numpy as np

# table[i][j] = the concatenation of (0-k) and (0-9) mod k
#TODO why are we doing above comment WHY O WHY!?!
def makeTable(k):
	table = [ [ int( str(x) + str(y) ) % k for y in range(10) ] for x in range(k) ]
	return table

# Returns if n is a multiple of the k used to generate the table
def isMultiple(dividend, table):
	state = 0
	for digit in dividend:
		state = table[state][int(digit)]
	if state == 0:
		return True
	return False


def isNotStrongMultiple(k, n):
	table = makeTable(k)
	if isMultiple(n, table):
		return False
	# for every digit in n, see if (n minus that digit) is a multible of k
	for digit in range(1,len(n)):
		if isMultiple(n[:-digit], table):
			print("The value: ",n[:-digit] ,", is divisible by: ",k)
			print("Test (value % 7) ==", int(n[:-digit]) % k)
			return False
	return True



#k = input("k: ")
#n = input("n: ")
k = 7
n = str(741842607938866199443579680083706254648829519399268)
print(isNotStrongMultiple(k, n))
