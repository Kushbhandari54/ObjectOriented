class Student:
    def __init__(self,aname,asalary,arole): # This is constructor 
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printDetail1(self):
        return f"The name is {self.name} and salary is {self.salary} and role is {self.role}"


harry=Student('harry','$2000','Teacher')

if __name__ == '__main__':
    print(harry.printDetail())