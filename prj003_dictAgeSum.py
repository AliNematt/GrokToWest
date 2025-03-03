myDict = {
    "Ali" : 28,
    "Reza" : 25,
    "Alireza" : 26
}

def dictAgeSum(myDict):
    ageSum = 0
    for item in myDict.values(): ageSum += item if isinstance(item, int) else False
    return ageSum

print(dictAgeSum(myDict))