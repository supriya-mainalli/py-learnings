def is_palindrome(mystr):
    left = 0
    right = len(mystr)-1
    while left<right:
        if mystr[left]!=mystr[right]:
            return False
        left+=1
        right-=1
    return True

print(is_palindrome('test'))
    