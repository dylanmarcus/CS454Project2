import re


def MinString(digits, k):
    table = [[0 for i in range(len(digits))] for i in range(2*k)]
    for i in range(k + k):
        for j in range(len(digits)):
            if i < k:
                table[i][j] = [int(str(i) + str(digits[j])) % k, i + k]
            else:
                table[i][j] = (int(str(i) + str(digits[j])) % k)
    return table


def makeNFA(k):
    NFA = MinString([i for i in range(10)], k)
    return NFA


def isStronglyDivisible(k, n):
    inputString = list(n)
    bools = []

    state = 0
    for i in range(len(inputString)):
        state = (state * 10 + int(inputString[i])) % k
        if state == 0:
            bools.append(1)
        else:
        	bools.append(0)

    for i in range(0, len(n)):
        inputString.pop(i)

        state = 0
        for i in range(len(inputString)):
            state = (state * 10 + int(inputString[i])) % k

        if state == 0:
            bools.append(1)
        else:
        	bools.append(0)
        inputString = list(n)

    if 0 in bools:
    	return 0
    return 1




def main():
    while True:
        try:
            problem = int(input("Which problem would you like to run: 1, 2, or 3 (0 to quit): "))
        except ValueError:
            continue
        if problem == 0:
            break
        if problem == 1:
            k = int(input("k: "))
            print(*makeNFA(k)[0: 9], sep='\n')
            n = input("n: ")
            if isStronglyDivisible(k, n):
                print("YES, " + n + " is strongly divisible by " + str(k))
            else:
                print("NO, " + n + " is not strongly divisible by " + str(k))

        if problem == 2:
            fileName = "words.txt"
            regex = ".*([a-zA-Z])" + '\\' + "1.*([a-zA-Z])" + '\\' + "2.*"
            print(regex)
            print("")
            pattern = re.compile(regex)
            for i, line in enumerate(open(fileName)):
                for match in re.finditer(pattern, line):
                    print(line)

        # if problem == 3:

main()