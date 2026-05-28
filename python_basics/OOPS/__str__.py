# the __str__() method is a special method that controls wht is returned when the object is printed.


#WITHOUT __str__()
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Noah",21)
print(p1)

#WITH __str__()
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
       return 3+4

p1=Person("Noah",21)
print(p1)