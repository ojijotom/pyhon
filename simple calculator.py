firstnumber =int(input("Enter  first number"))
secondnumber =int(input("Enter second number "))
operator =input("Enter operator(*,/,-,+,)")

if operator== "+":
    answer=(firstnumber+secondnumber)
    print(answer)

elif operator=="-":
    answer =(firstnumber-secondnumber)
    print(answer)

elif operator=="*":
    answer =(firstnumber*secondnumber)
    print(answer)

elif operator=="/":
    answer =(firstnumber/secondnumber)
    print(answer)

else :
    print("Math error")



