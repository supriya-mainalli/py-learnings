# dir(names)
names = ['vinod', 'manju', 'maruthi', 'ria']

#Add an item at last
names.append("supriya")

# Remove an item
names.remove("ria")

# Pop will remove the last element and returns the popped item
names = ['vinod', 'manju', 'maruthi', 'supriya']
print(names.pop()) # returns supriya

# Pop particular item
names = ['vinod', 'manju', 'maruthi', 'supriya']
print(names.pop(2)) # 'maruthi'

# adding element at particular index
names=['vinod', 'manju', 'ria', 'maruthi', 'john', 'priya']
names.insert(2, 'supriya')
print(names) #['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya']

# List concatination
names = ['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya']
names+=["chetan"]
print(names) #['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya', 'chetan']

names += "test"
print(names) #['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya', 'chetan', 't', 'e', 's', 't']
""" List comprehensions"""

names = ['vinod', 'manju', 'maruthi', 'ria']

names = [d.upper() for d in names]


""" Return value if the item is int or float and the value is even number"""

data = [45, 9874, 'jfgh', 'ufdf', 56,0.98]
data = [x for x in data if type(x) in (int,float) and x%2==0]


print(data, names)