class Parent:
    def __init__(self):
        print("iam parent class")
class Child(Parent):
    def __init__(self):
        print("iam child class")
    @classmethod
    def m2(cls):
        print("iam the class method of class")
c=Child()
p=Parent()
#2nd case
class Parent:
    def __init__(self):
        print("iam parent class")
    def m2(self):
        print("this is parent method")
class Child(Parent):
    def m1(self):
        print("iam child class")
sai=Child()
sai.m1()
sai.m2()
#3rd case using super function
class Parent:
    def __init__(self):
        print("iam parent class constructor")
    def m2(self):
        print("this is parent method")
class Child(Parent):
    def __init__(self):
        super().__init__()
        super().m2()
        print("iam the child class constructor")
    def m1(self):
        super().m2()
        print("iam child class method")
v=Child()
v.m1()
