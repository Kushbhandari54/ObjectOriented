class Employee:
    #no_of_leaves is a class varible
    no_of_leaves=10
    pass

harry=Employee()
larry=Employee()

# name and salary are instance variable
harry.name="Harry"
harry.salary="$600"

larry.name="Name"
larry.salary="$500"

print(harry.no_of_leaves)
print(larry.no_of_leaves)

print(Employee.no_of_leaves)

print(harry.name)
print(larry.name)

harry.no_of_leaves=12
larry.no_of_leaves=15

print(harry.no_of_leaves)
print(larry.no_of_leaves)

print(larry.__dict__)

