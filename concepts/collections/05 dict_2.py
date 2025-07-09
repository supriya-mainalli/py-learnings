p1 = {'name': 'supriya', 'city': 'bangalore', 'email': 'abc@gmail.com', 'city2': 'mumbai'}

print(p1) # {'name': 'supriya', 'city': 'bangalore', 'email': 'abc@gmail.com', 'city2': 'mumbai'}
print(p1['name']) # supriya

p1.clear()
print(p1)

p1 = dict(name='suppi', city='bangalore', email='abs@jfhd.com')
print(p1) #{'name': 'suppi', 'city': 'bangalore', 'email': 'abs@jfhd.com'}

print(p1.keys()) #dict_keys(['name', 'city', 'email'])

print(p1.values()) #dict_values(['suppi', 'bangalore', 'abs@jfhd.com'])

print(p1.items()) # dict_items([('name', 'suppi'), ('city', 'bangalore'), ('email', 'abs@jfhd.com')])

# by default if we don't provide items it print keys
for k in p1:
    print(k)
# name
# city
# email


# iterating dict2

for k,v in p1.items():
    print(f"The key is {k} and value is {v}")
# The key is name and value is suppi
# The key is city and value is bangalore
# The key is email and value is abs@jfhd.com

p2 = {'address':'123'}
p1.update(p2)
print(p1) # {'name': 'suppi', 'city': 'bangalore', 'email': 'abs@jfhd.com', 'address': '123'}

# for pop, we need to pass keys and it returns popped value

a = p1.pop('name')
print(a) # suppi