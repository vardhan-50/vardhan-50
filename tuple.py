tuple=()
tuple=tuple+(10,20,30,40,50)
print(tuple)
x=int(input('Enter the element that you want delete:'))
y=int(input('Enter the index position present in tuple:'))
deleted_element=()
for item in tuple:
    if item != x:
        deleted_element +=(item,)
print(deleted_element)
if y in tuple:
    position=tuple.index(y)
    print(position)
else:
    print(f'{y} is not in tuple')
