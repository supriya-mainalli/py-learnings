class Person:

    def __init__(self,x,y):
        self._x = x
        self._y = y

    # we can call this method same as instance varible p.get_x_val
    @property 
    def val_x(self):
        return self._x
    
    # setter methods where we pass the varibale to set
    @val_x.setter
    def val_x(self, val):
        self._x = 20+val

p = Person(10, 20)
print(p._x)
print(p._y)
print(p.val_x)
p.val_x = 30
print(p.val_x)
    