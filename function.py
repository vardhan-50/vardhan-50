#1
def school(y):
    print("schools are opened")
school(2)
#2
def course(a):
    print('Welcome to course name')
course(1)
#3
def even(x):
    a=tuple(range(0,x,2))
    return a
result=even(10)
print(result)
#4
def odd(x):
    a=list(range(1,x,2))
    return a
result=odd(10)
print(result)
#5
def arithmatic(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
arithmatic(3,4)
#6
def store(x):
    a=list(range(x))
    return a
result=store(10)
print(result)
#7
def concat(x,y):
    print(x+y)
concat('PALLE','TECHNOLOGIES')