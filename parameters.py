def details(name,**subjects):
    print(name)
    for i in subjects:
        print(i,subjects[i])
details("vardhan",python=25,mysql=25,oops=30)