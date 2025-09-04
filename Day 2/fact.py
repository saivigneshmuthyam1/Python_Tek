def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
    
a=int(input("enter a number to find factorial:"))
print("factorail of",a,"is",fact(a))