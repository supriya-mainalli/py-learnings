def str_comp_exp(mystr):
    l = 0
    r = 0
    n = len(mystr)
    res = ""
    while(r<n):
        if mystr[r]!= mystr[l] and r!=n-1:
            res = res + mystr[l] + str((r-1)-l+1)
            l = r
        r = r+1
        if r==n-1:
            res = res +mystr[l] + str((r-l)+1)

    return res
print(str_comp_exp("abbccc"))
