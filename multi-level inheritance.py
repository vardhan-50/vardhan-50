class Grandparent():
    def m1(self):
        print("hello")
class Parent(Grandparent):
    def m2(self):
        print("hii")
class Child(Parent):
    def m3(self):
        print("hello everyone")
c=Child()
c.m1()
c.m2()
c.m3()