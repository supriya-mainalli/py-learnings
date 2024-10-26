# String are immutable objects

# String Concatenation
str1 = "Hello"
result = str1 + " " + "world"
print(result)  # Hello world

# String repetition

str1 = "test"
result = str1 * 3
print(result)  # testtesttest

# join string from tuple, list
my_list = ["supriya", "maruthi", "vinod", "reshma"]
str2 = "*".join(my_list)
print(str2)  # supriya*maruthi*vinod*reshma

t1 = tuple(my_list)
str2 = "###".join(t1)
print(str2)  # supriya###maruthi###vinod###reshma

# String slicing
str3 = "Hello there, welcome to python"
print(str3[2:])  # llo there, welcome to python i.e include from index 2 and rest evrything else

print(str3[::-1])  # nohtyp ot emoclew ,ereht olleH
str3[2] = "y"  # TypeError: 'str' object does not support item assignment

print(str3[::-2]) # nhy teolw,rh le