# Python Is Easy homework. If statements

def checkEqualityOfTwo(var1, var2, var3):
    
    if var1.isdigit() == True:
        var1 = int(var1)

    if var1 == var2 or var1 == var3:
        return True
    elif var1 == var2 or var1 == var3:
        return True

    if var2 == var1 or var2 == var3:
        return True

    if var3 == var1 or var3 == var2:
        return True

    return False


if checkEqualityOfTwo("4", 4, 4) == True:
    print("At least two values are equal")


if checkEqualityOfTwo(1, 5, 8) == False:
    print("No equal values")



    
