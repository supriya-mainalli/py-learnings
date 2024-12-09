def isAnagram(mystr1, mystr2):
    l1 = list(mystr1)
    l2 = list(mystr2)
    print(l1.sort() == l2.sort())
    if l1.sort() == l2.sort():
        return True
    return False


print(isAnagram('racecar2', 'carrace'))
