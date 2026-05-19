class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Hi my name is {self.name}")
        print(f"lets print value {self}")
    
    def greet(self):
        print(f"And my age is {self.age}")
        print(f"the value of s is {self}")

p1 = Person()
p2 = Person()
p1.set_details('rohan',20)
p1.display()
p1.greet()
p2.set_details('jack',10)
p2.display()
p2.greet()