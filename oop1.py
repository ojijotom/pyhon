from classobject import student1


class Student:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def study(self):
        print(self.name,"is studying")

student1 =Student("Innocent","male",26)
print(student1.name,student1.gender,student1.age)
student1.study()
student2 =Student("Abigael","Female",25)
print(student2.name,student2.gender,student2.age)
student2.study()

student3 =Student("Mercy","Female",36)
print(student3.name,student3.gender,student3.age)
student3.study()

student4 =Student("Tom","male",27)
print(student4.name,student4.gender,student4.age)
student4.study()

student5 =Student("Morrine","Female",22)
print(student5.name,student5.gender,student5.age)
student5.study()
