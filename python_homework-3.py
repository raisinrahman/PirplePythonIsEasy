# Python Is Easy homework. If statements

"""
Check for equality of at least 2 numbers
"""
def checkEqualityOfTwo(var1, var2, var3):
    
    """
    Extra credit.  If number strings are passed
    convert to integers before comparing
    """
    if type(var1) == str:
        var1 = int(var1)

    if type(var2) == str:
        var2 = int(var2)

    if type(var3) == str:
        var3 = int(var3)

    if var1 == var2 or var1 == var3:
        return True

    if var2 == var1 or var2 == var3:
        return True

    if var3 == var1 or var3 == var2:
        return True

    return False


"""
Pass in a number string
"""
if checkEqualityOfTwo("4", 12, 4) == True:
    print("At least two values are equal")


if checkEqualityOfTwo(1, 10, 12) == False:
    print("No equal values")



    
