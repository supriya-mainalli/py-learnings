class Person:
    def get_details(self):
        self.name = "john"
        self.age = 30

    def dispaly(self):
        print("Hi this is display method", self)

    def greet(self):
        print("Hello good morning")


p1 = Person()
print(p1.get_details)
