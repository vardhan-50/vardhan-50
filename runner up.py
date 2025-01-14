num=int(input())
list1=[]
for i in range(1,num+1):
    a=int(input())
    list1.append(a)
unique_list=list(set(list1))
unique_list.sort()
if len(unique_list) >= 2:
    print(unique_list[-2])
