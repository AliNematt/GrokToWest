def listReverse(myList):
    reversedList = []
    for item in myList:
        reversedItem = ""
        for index in range(len(item)-1,-1, -1): reversedItem += item.casefold()[index]
        reversedList.append(reversedItem.capitalize())
    return reversedList
            
myList = ["World", "Life", "Galaxy", "Dreams", "Imagination"]
reversedList = listReverse(myList)
