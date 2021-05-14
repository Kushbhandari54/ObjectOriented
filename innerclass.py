class A:
    def __init__(self):
        self.name="A"
        self.obj2=self.B()

    def property1(self):
        print("This is property of class A")
    
    class B:
        def property2(self):
            print("This is property of class B")
        
obj1=A()
obj1.obj2.property2()
