class Student:
    def details(self,name):
        print(f"{name} good morning")
        Student.course("Nandyal")
        Student.sum(4,5)
    @classmethod
    def course(cls,place):
        print(f"hello palle and {place}")
        Student.sum(10,20)
    @staticmethod
    def sum(a,b):
        print(a+b)
        #Student.course("sanjamala")#we can access but as per industry rule, it is not recommended
s=Student()
s.details("sai")
Student.course("bengaluru")
s.sum(2,5)