# Python Is Easy homework. Lists

myUniqueList = []
myLeftOvers = []

"""
Add any thing to my list.  As long
as it is unique
"""
def addToMyList(valueToAdd):
    if valueToAdd in myUniqueList:
        myLeftOvers.append(valueToAdd)
        return False
    else:
        myUniqueList.append(valueToAdd)
        return True


# Add stuff to the list

addToMyList("Rodney")
addToMyList("Oliver")
addToMyList("Children")
addToMyList(["Emilee", "Aidan"])
addToMyList("Rodney")
addToMyList([16, 12])
addToMyList(["Emilee", "Aidan"])
addToMyList(12)

print(myUniqueList[3])
print(myUniqueList[3:])
print(myUniqueList[4][-1])
print(myUniqueList)

print("\n===The Left Overs===")
print(myLeftOvers)




