from __future__ import print_function


def makeNFA(k):
	NFA = [[ [] for i in range(10)] for i in range(k*2)]
	for i in range(k):
		for j in range(10):
			NFA[i][j].append(int( str(i) + str(j) ) % k)
			NFA[i+k][j].append(int( str(i) + str(j) ) % k)
			
	for i in range(k):
		for j in range(10):
			NFA[i][j].append(i + k)

	return NFA


NFA = makeNFA(3)

# Print out NFA just so we can visualize it
for i in range(6):
	print(str(i) + "| ", end='')
	for j in range(10):
		print(" " + str(NFA[i][j]) + " ", end='')
	print('\n')