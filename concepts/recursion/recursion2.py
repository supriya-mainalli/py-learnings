# print name in n times

# def main():
#     func1(i, n)



def func1(i, n):
    if(i>n):
        return
    print('supriya')
    func1(i+1, n)

# if __name__ == '__main__':
    # main()

# func1(1, 3)

def fib(num):
    if num == 0:
        return 1
    return num*fib(num-1)

n = 0
# print(fib(n))

def test(s):
    prefix = ''
    newstr = ''
    for i in s:
        if(i.isdigit() and int(i)!=0):
            newstr = newstr+i
            print(f"the iteration is {newstr}")
        elif (i=='-' or i=='+'):
            prefix = i
        else:
            print('it has char')

    if prefix:
        newstr = (prefix*1)*int(newstr)
        print(newstr, type(str))
    print(newstr)
    return int(newstr)

print(test("1337c0d3"))
