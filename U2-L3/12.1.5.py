class Person:
    def __init__(self, name):
        self.__name = name
        self.name = name
    def altToprivate(self,new_value):
        if len(str(new_value)) >= 10:
            self.__name = str(new_value)
    def __str__(self):
        return self.__name
A = Person("210210")
print(A)
A.altToprivate(12093128032)
print(A)
