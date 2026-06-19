# key value pair

my_dict = {'name':'supriya','city':'bengaluru','class':'10','marks':90}

keys = my_dict.keys()
values = my_dict.values()

for k,v in my_dict.items():
    print(f'the key is {k} and value is {v}')

# print(my_dict.items()) #dict_items([('name', 'supriya'), ('city', 'bengaluru'), ('class', '10'), ('marks', 90)])

# update the dict

my_dict.update({'state':'KA'})

# print(my_dict)


my_dict = {'name': 'khushi', 'city': 'bangalore', 'pin': 1234}

for item in my_dict.items():
    print(f'key is {item[0]}, value is {item[1]}')

# print(my_dict.keys())
# print(my_dict.values())

people = [{'name' : 'supriya', 'city': 'bangalore'}, {'name' : 'manju', 'city': 'bangalore123'}]

for item in people:
    if item['name'] =='supriya':
        print(item)

l1 = ['name', 'age', 'city']
l2 = ['supriya', 30, 'bangalore']

my_dict = {}
for data in zip(l1,l2):
    print(data)

print(list(zip(l1,l2))) # [('name', 'supriya'), ('age', 30), ('city', 'bangalore')]
print(dict(list(zip(l1,l2)))) # {'name': 'supriya', 'age': 30, 'city': 'bangalore'}
    
print(dict(zip(l1,l2)))