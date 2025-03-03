def printLines(file):
    lineNumber = 0
    for index in file.readlines():
        lineNumber += 1
        print(f"{lineNumber} => {index}")

with open("poem.txt", "r") as file: printLines(file)
