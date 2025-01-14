#method overriding
class Animal:
    def walk(self):
        print("Animal will walk by 4 legs")
class Human(Animal):
    def walk(self):
        print("Human will walk by 2 legs")
h=Human()
h.walk()
#method overloading
#python doesn't support method overloading,because
# python will consider only latest method and also python have arbitrary parameter
class Rbi:
    def set_interest(self,x):
        print("minimum interest is 10%")
class Sbi(Rbi):
    def set_interest(self,y,z):
        print("sbi,follow rbi rules")
s=Sbi()
(s.set_interest(2,3))
