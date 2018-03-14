import numpy as np


# Generates table of k by 10 in size.
# table[i][j] = the concatenation of (0-k) and (0-9) mod k
def makeTable(k):
	table = [[None for i in range(10)] for i in range(k)]
	for i in range(k):
		for j in range(10):
			table[i][j] = int( str(i) + str(j) ) % k
	return table


# Returns if n is a multiple of the k used to generate the table
def isMultiple(n, table):
	state = 0
	for digit in n:
		state = table[state][int(digit)]
	if state == 0:
		return True
	return False


def isNotStrongMultiple(k, n):
	table = makeTable(k)
	if isMultiple(n, table):
		return False
	# for every digit in n, see if (n minus that digit) is a multible of k
	for digit in range(len(n)):
		if isMultiple(n[:digit] + n[digit+1:], table):
			return False
	return True



k = input("k: ")
n = input("n: ")
print isNotStrongMultiple(k, str(n))