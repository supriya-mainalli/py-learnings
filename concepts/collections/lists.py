""" List comprehensions"""

names = ['vinod', 'manju', 'maruthi', 'ria']

names = [d.upper() for d in names]


""" Return value if the item is int or float and the value is even number"""

data = [45, 9874, 'jfgh', 'ufdf', 56,0.98]
data = [x for x in data if type(x) in (int,float) and x%2==0]


print(data, names)