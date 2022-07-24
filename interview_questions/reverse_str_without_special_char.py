# https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

mystr = "Ab,c,de!$"
mystr = list(mystr)
reverse_str = ""
special_char = "$/&!*,"

for item in mystr:
    if item not in special_char:
        reverse_str = item + reverse_str

print("Reversed string is {}".format(reverse_str))
j = 0
while j < len(reverse_str):
    for i in range(len(mystr)):
        if mystr[i] not in special_char:
            mystr[i] = reverse_str[j]
            j += 1

print("".join(mystr))
