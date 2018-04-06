import queue

def makeNFA (k):

    NFA = [[ [] for i in range(10)] for i in range(2*(k+1))]
    # traverse through NFA and populate it
    for i in range(k+1):
        for j in range(10):
            if i == 1:
                NFA[i][j].append((int(str(i-1) + str(j)) % k) + 1)
                NFA[i+k+1][j].append((int(str(i - 1) + str(j)) % k) + 2)
            else:
                NFA[i][j].append((int(str(i) + str(j)) % k) + 1)
                NFA[i + k + 1][j].append((int(str(i) + str(j)) % k) + 2)

    for i in range(k+1):
        for j in range(10):
            NFA[i][j].append(i + k + 1)

    # print all states
    print("Accepting States: [1,", str(k+2) + "]")
    for i in range(0, (2*k)+2):
        print(str(i) + ') ', end='')
        for j in range(10):
            print(NFA[i][j], end=' ')
        print("")

    return NFA


def divisible(k, n):
    # create NFA
    table = makeNFA(k)
    # Create a list to store states visited
    visited = []
    for i in range(0, 2 * (k+1)):
        visited.append(0)
    boolList = []
    # Create queue to fill with states needing to be checked
    q = queue.Queue()
    state = 0
    q.put([state, str(n)])
    while not q.empty():
        object = q.get()

        state = object[0]
        symbol = int(object[1][0])

        if len(object[1]) == 1:
            for element in table[state][symbol]:
                if element == 1 or element == k+2:
                    boolList.append(1)
                else:
                    boolList.append(0)
        else:
            for element in table[state][symbol]:
                t = object[1][1:]
                q.put([element, t])

    return boolList


k = int(input("k: "))
n = int(input("n: "))
listOfBool = divisible(k, n)
if True in listOfBool:
    print("YES, " + str(n) + " is strongly divisible by " + str(k))
else:
    print("NO, " + str(n) + " is not strongly divisible by " + str(k))
