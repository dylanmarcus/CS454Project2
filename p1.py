def MinString(d_values, k_value):


# This makes our DFA table using the d_values which is 0-9
grid = [[0 for x in range(len(d_values))] for y in range(k_value + k_value)]
for i in range(k_value + k_value):
    for j in range(len(d_values)):
        if i < k_value:
            grid[i][j] = [int(str(i) + str(d_values[j])) % k_value, i + k_value]
        else:
            grid[i][j] = (int(str(i) + str(d_values[j])) % k_value)
return grid


def make_NFA(k_Value):
    NFA = MinString([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k_Value)
    print("Printing NFA")
    print(*NFA[0: 9], sep='\n')


def strongly_divisible(k_value):
    make_NFA(k_value)

    # store N in an array
    n_value = raw_input("Input an integer N\n")
    val_list = list(n_value)

    # checks the first number to see if it is strongly divisible
    current = 0
    for i in range(len(val_list)):
        current = (current * 10 + int(val_list[i])) % k_value
        if current == 0:
            return 1

    # will remove one number at a time from the input N and check each sub
    # number to see if it is strongly divisble
    for i in range(0, len(n_value)):
        val_list.pop(i)

        # checks to see if the sub number is strongly divisble
        # Long version of moding a number
        current = 0
        for i in range(len(val_list)):
            current = (current * 10 + int(val_list[i])) % k_value

        if current == 0:
            return 1
        val_list = list(n_value)


k = int(input("k: "))
strongly_divisible(k)