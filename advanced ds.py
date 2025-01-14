list=['sai','hi','hello','hi','sai','hi','hello','sai']
dic={}
for i in list:
    count=1
    if i not in dic:
        dic[i]=count
    else:
        count +=1
        dic[i]=count
print(dic)
x=['a','b','c','d']
y=[10,20,30,40]
tup=[]
for i in range(len(x)):
    a=[x[i],y[i]]
    tup.append(a)
print(tup)