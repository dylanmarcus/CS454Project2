import numpy as np


"""
table is an NFA that rejects any int (as a string) that is not
divisible by k, where table[i] is an NFA stateand table[j] is
the transition on any given state. So table[i][j] determines
what state will be reached, given a transition.
"""
def makeTable(k):
	table = [[None for i in range(10)] for i in range(k)]
	for i in range(k):
		for j in range(10):
			table[i][j] = int( str(i) + str(j) ) % k
	return table


# function to traverse an NFA, given a string n
def isMultiple(n, table):
	# state 0 is the starting and accepting state in all cases
	state = 0
	for digit in n:
		state = table[state][int(digit)]
	if state == 0:
		return True
	return False


def isNotStrongMultiple(k, n):
	table = makeTable(k)
	accepted = []
	accepted.append(isMultiple(n, table))
	# remove each digit from n (one at a time), resulting in Nj
	# and run Nj through the NFA
	for digit in range(len(n)):
		accepted.append(isMultiple(n[:digit] + n[digit+1:], table))
	if True in accepted:
		print("no")
	else:
		print("yes")

	"""
	-MORE EFFICENT VERSION BUT INSTRUCTIONS SAY TO USE A LIST OF BOOLS-
	table = makeTable(k)
	if isMultiple(n, table):
		return False
	# remove each digit from n (one at a time), resulting in Nj
	# and run Nj through the NFA
	for digit in range(len(n)):
		if isMultiple(n[:digit] + n[digit+1:], table):
			return False
	return True
	"""



k = input("k: ")
n = input("n: ")
isNotStrongMultiple(k, str(n))