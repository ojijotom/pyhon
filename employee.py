from functions import employee


class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(self.position,"is earning salary",self.salary)

employee1 = Employee("John","CEO",320000)
print(employee1.name,employee1.position,employee1.salary)
employee1.info()

employee2 = Employee("Jane","Managing Director",730000)
print(employee2.name,employee2.position,employee2.salary)
employee2.info()

employee3 = Employee("Tom","Software Engineer",540000)
print(employee3.name,employee3.position,employee3.salary)
employee3.info()

employee4 = Employee("Peter","CEO",450000)
print(employee4.name,employee4.position,employee4.salary)
employee3.info()
employee5 = Employee("Abraham","CEO",660000)
print(employee5.name,employee5.position,employee5.salary)
employee5.info()