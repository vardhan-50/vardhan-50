class Student:
    course="python"
    def study(self,sub):
        self.sub=sub
        print(self.sub)
        print(Student.course)
    def m2(self):
        print(self.sub)#4
        print(Student.add(3, 4))  # 14
        print(self.course)  # 1
    @classmethod
    def exam(cls,date):
        print(cls.course)#2
        print(date)#7
        print(Student.add(2,3))# 10 and 15

    @staticmethod
    def add(a,b):
        print(Student.course)#3 but this not recommended as per industry rule.
        #print(Student.exam("27-10-2001"))#13
        #print(Student.)
        print(a+b)
s=Student()
print(s.exam("01-01-25"))

