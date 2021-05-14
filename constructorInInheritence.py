class A:
    def __init__(self):
        print("We are in A class")

    def property1(self):
        print("property of class A")

class B:
    def __init__(self):
        print("we are in class B")

    def property1(self):
        print("property of class B")

class C(A,B):
    def __init__(self):
        super().__init__()        #it will always  take values from the left  to right
        print("We are in C class")

    def property3(self):
        super().property1()
        

obj1=C()
obj2=B()
obj2.property1()
obj1.property3()
