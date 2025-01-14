class Animal():
    def sound(self):
        print("animal will make sound")
class Dog(Animal):
    def bark(self):
        print("dog will bark")
c=Dog()
c.sound()
c.bark()

