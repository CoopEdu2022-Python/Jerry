class A:
    def __init__(self):
        self.__a = 1
    def change_private(A,key):



class B(A):
    def __init__(self):
        self.__b = 2
    def change_private(A,new_value):
        
b = B
b.change_private("",3)
print('\n'.join(['{0}: {1}'.format(item[0], item[1]) for item in b.__dict__.items()]))