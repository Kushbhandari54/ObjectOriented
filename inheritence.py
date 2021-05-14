'''
class A:
    # this is single level Inheritance
    def property1(self):
        print("this is property 1")
    def property2(self):
        print("this is property 2")


#class B inherit class A property   
# Class B is sub class of A class
class B(A):
    def property3(self):
        print("This is property 3")

    def property4(self):
        print("This is property 4")

obj1=A()
obj2=B()
obj2.property1()
obj2.property2()
'''

'''
 # this is multi level Inheritance
class A:
    def property1(self):
        print("this is property 1")
    def property2(self):
        print("this is property 2")


#class B inherit class A property   
# Class B is sub class of A class

class B(A):
    def property3(self):
        print("This is property 3")

    def property4(self):
        print("This is property 4")
#Now class C inherit property of Class A and Class B both.

class C(B):
    # this is single level Inheritance
    def property5(self):
        print("this is property 5")
    def property6(self):
        print("this is property 6")
obj1=A()
obj2=B()
obj3=C()

obj3.property1()
obj3.property2()
obj3.property3()
obj3.property4()

'''
 # this is multiple  Inheritance
class A:
    def property1(self):
        print("this is property 1")
    def property2(self):
        print("this is property 2")

class B:
    def property3(self):
        print("This is property 3")

    def property4(self):
        print("This is property 4")

class C(A,B):
    def property5(self):
        print("this is property 5")
    def property6(self):
        print("this is property 6")
obj1=A()
obj2=B()
obj3=C()

obj3.property1()
obj3.property2()
obj3.property3()
obj3.property4()
