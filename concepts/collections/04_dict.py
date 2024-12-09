# key value pair

my_dict = {'name':'supriya','city':'bengaluru','class':'10','marks':90}

keys = my_dict.keys()
values = my_dict.keys()

for k,v in my_dict.items():
    print(f'the key is {k} and value is {v}')

print(my_dict.items()) #dict_items([('name', 'supriya'), ('city', 'bengaluru'), ('class', '10'), ('marks', 90)])

# update the dict

my_dict.update({'state':'KA'})

print(my_dict)
