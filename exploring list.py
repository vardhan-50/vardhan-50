list=[]
for i in range(1,11):
    a=int(input('enter the element:'))
    list.append(a)
print(list)
pos=int(input("enter the position:"))
ele=int(input("enter the element:"))
list.insert(3,300)
print(list)
dele=int(input("enter the element that you want delete:"))
if dele in list:
    list.remove(dele)
    print(list)
else:
    print("The given element is not present in list")
posi=int(input("enter the position that you want delete:"))
if posi in list:
    list.pop(posi)
    print(list)
else:
    print("The given position is not present in list")
index=int(input("enter the index value:"))
if index in list:
    print(list.index(index))
    print(list)
else:
    print("The given index value is not present in list")



