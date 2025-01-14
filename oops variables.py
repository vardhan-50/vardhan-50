#local variable
class Student:
    def study(self,subject):
        print(f"The subject is:{subject}")
s=Student()
s.study("python")
#instance variable
class Teacher:
    def teach(self):
        self.language="mysql"
        print(self.language)
t=Teacher()
t.teach()
print(t.language)
#class variable
class Crop:
    farm="red chilli"
    def farming(self):
        print("A farmer can do farming")
c=Crop()
print(Crop.farm)
print(c.farm)