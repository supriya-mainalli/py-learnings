# Pattern1

# * * * *
# * * * *
# * * * *
# * * * *
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=" ")
        print("\n")

# print(pattern1(5))


# *
# * *
# * * *
# * * * *

def pattern2(n):
    for i in range(1, n+1):
        for j in range(i): # since range(0) is []
            # print('*', end = ' ')
            print(j+1, end = ' ')
        print()
# print(pattern2(4))

def pattern3(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=' ')
        print()
print(pattern3(5))

