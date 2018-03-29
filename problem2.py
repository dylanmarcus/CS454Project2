import re

# using 're' to run grep/regexp commands through python
# to run on command line, use:
# grep -E '.*([a-zA-Z])\1.*([a-zA-Z])\2.*' ./words.txt > output.txt
# this will output all the correct expressions to a file called output.txt in your cwd


# ignore this line -- previous tests -- (\w*(\w)\2\w*){2,}|(\w)\3{2}

def main():
    print ("This program will find words that have at least two occurrences of\nthe same letter next to each other occurring at least twice\n")
    while True:
        try:
            fileName = input("Please enter a .txt file that contains a list of different words\n")
        except ValueError:
            continue
        if fileName.find(".txt"):
            break
    regex = ".*([a-zA-Z])" + '\\' + "1.*([a-zA-Z])" + '\\' + "2.*"
    pattern = re.compile(regex)
    for i, line in enumerate(open(fileName)):
        for match in re.finditer(pattern, line):
            print(line)


main()
