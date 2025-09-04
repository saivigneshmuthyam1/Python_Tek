def sum(a):
    if a==0:
        return 0
    else:
        return a+sum(a-1)
    
a=int(input("enter a number"))
print("Sum of natural number up to",a,"is",sum(a))