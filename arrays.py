courses = ["MIT","Cybersecurity","Datascience"]
print(courses)


# Accessing an element
print(courses[2])


# Looping through an array
for x in courses :
    print("course is",x)

# Adding a new element into an array
courses.append("Laravel")
print(courses)


# Removing an element from an array
courses.remove("Cybersecurity")
print(courses)