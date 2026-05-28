class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.age=23
s1=Student("dishmitha","chintagunta")
print(s1.age)

#multiple and multi-level inheritance:
# Multiple Inheritance: A class inherit methods and properties from more than one class
#Multi-level Inheritance: A class inherit form a class which inherit form another class

class India:
    def sta(self):
        print("this state belongs to india")
class Bihar(India):
    def __init__(self,sname):
        self.sname=sname
class patna(Bihar):
    def __init__(self,sname,cityname):
        super().__init__(sname)
        self.cityname=cityname
    def display(self):
        print(f"capital city of {self.sname} is {self.cityname}")
s1=Bihar("Bihar")
c1=patna("Bihar","Patna")
c1.display()
c1.sta()

#Duck typing: another type to achieve polymorphism besides inheritance

class Animals:
    alive=True
class Dog(Animals):
    def speak(self):
        print("woof")
class Cat(Animals):
    def speak(self):
        print("Meow")
class Car:
    def speak(self):
        print("hork")
    alive=False

am=[Cat(),Car(),Dog()]
for p in am:
    p.speak()
    p.alive