# Built-In function /Standard Library-Function

y = max(45,66,78,87,99,78,65)
print("The maximum value is",y )

x =min(46,98,67,33,32,34,21)
print("The minimum value is",x)



# User-defined Functions
def school():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1 + num2)

add()

#Parameter/Variable and Argument/Value
def multiply(a,b):
    print(a * b)

multiply(6,5)
multiply(3,4)
multiply(7,8)



def employee(name,age,gender,salary,position):
    print(name,age,gender,salary,position)

employee("Morrine",25,"Female",500000,"ceo")
employee("Ojijo",20,"Male",50000,"ceo")
employee("Mark",22,"Male",50000,"ceo")
employee("Abii",21,"Female",50000,"ceo")
employee("John",26,"Male",50000,"ceo")
employee("Josse",30,"Male",50000,"ceo")
employee("Mica",19,"Male",50000,"ceo")
employee("Lora",27,"Female",50000,"ceo")
employee("Jimmy",24,"Male",50000,"ceo")



#A program to display details of 5 patients
# Using a User-defined function , implement parameter
#and argument
#fullname, gender, age , disease


def patients(fullname,gender,age,disease):
    print(fullname,gender,age,disease)


patients("Mark","Male",20,"Malaria")
patients("John","Male",19,"Hepatitis")
patients("Jimm","Male",18,"Typhoid")
patients("Tom","Male",24,"Syphilis")
patients("Cliff","Male",25,"Corona")
