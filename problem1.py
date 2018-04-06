from __future__ import print_function


def makeNFA(k):
	# A DFA to that accepts multiples of k has k+1 states where the starting
	# state q0 has identical transitions as q1, where q1 is the accepting state.
	# This is so the DFA does not accept the null string.
	# The NFA to solve the problem is made of 2 copies of the DFA.
	NFA = [[ [] for i in range(10)] for i in range((k+1)*2)]
	for i in range(k+1):
		for j in range(10):
			# q0 and q1 (of each of the two sub-DFAs) have identical transitions
			if i == 1:
				NFA[i][j].append((int( str(i-1) + str(j) ) % k) + 1)
				NFA[i+k+1][j].append((int( str(i-1) + str(j) ) % k) + k + 2)
			else:
				NFA[i][j].append((int( str(i) + str(j) ) % k) + 1)
				NFA[i+k+1][j].append((int( str(i) + str(j) ) % k) + k + 2)
	# Each state of the first sub-DFA has additional transitions (on 0-9) to
	# their corresponding states of the second sub-DFA.
	for i in range(k+1):
		for j in range(10):
			NFA[i][j].append(i + k + 1)

	return NFA


NFA = makeNFA(3)

# Print out NFA just so we can visualize it
for i in range(8):
	print(str(i) + "| ", end='')
	for j in range(10):
		print(" " + str(NFA[i][j]) + " ", end='')
	print('\n')