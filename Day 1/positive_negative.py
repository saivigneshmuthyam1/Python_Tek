def pn(a):
    if a>0:
        return "POSTIVE"
    elif a<0:
        return "NEGATIVE"
    else:
        return "NOT NEGATIVE NOR POSTIVE"
        
a=int(input("Enter a number: "))
print("The number",a,"is",pn(a))