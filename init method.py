class Calculator:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def add_method(self,a,b):
        print(a+b)
    def sub_method(self,c,d):
        print(c-d)
c=Calculator('sai','vardhan')
print(c.fname)
print(c.lname)
c.add_method(4,5)
c.sub_method(10,7)

