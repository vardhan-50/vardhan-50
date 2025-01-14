class Animal:
    def eat(self):
        print("animal will eat")
class Dog(Animal):
    def bark(self):
        print("dog will bark")
class Cat(Animal):
    def eating(self):
        print("cat will eat and bark")
c=Cat()
c.eat()
c.eating()
d=Dog()
d.bark()
d.eat()