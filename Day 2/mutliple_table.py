def table(a,b):
    for i in range(b+1):
        print(a,"X",i,"=",a*i)

a,b=map(int,input("Enter which table and till where:").split())
table(a,b)