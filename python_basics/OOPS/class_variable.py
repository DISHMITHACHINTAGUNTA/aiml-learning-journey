class Student:
    graduate_year=2027
    num_students=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_students+=1
s1=Student("Dishmitha",20)
s2=Student("Nandini",21)
s3=Student("Geetha Lalitha",22)
print(f"My graduating year is {Student.graduate_year} with total {Student.num_students} students:")
print(s1.name)
print(s2.name)
print(s3.name)

