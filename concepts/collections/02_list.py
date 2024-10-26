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

# list extend will not add a lsit into list. 
names.extend(['test2'])
print(names) # ['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya', 'chetan', 't', 'e', 's', 't', 'test2']

#appending list obj
names = ['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya']
names.append(['test3'])
print(names) #['vinod', 'manju', 'supriya', 'ria', 'maruthi', 'john', 'priya', ['test3']]