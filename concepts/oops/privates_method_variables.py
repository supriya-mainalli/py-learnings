class Person:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z=30

    def methodA(self):
        pass

    def _methodB(self):
        return 'hi im method b'
    
    def __methodC(self):
        return 'this is double underscore method'


p = Person()
print(p._y)
print(p.methodA())
print(p._methodB())
print(p._Person__methodC()) #accessible
print(p.__methodC()) # we get AttributeError: 'Person' object has no attribute '__methodC'




        