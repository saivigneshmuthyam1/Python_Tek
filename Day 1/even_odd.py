def eoro(a):
    if a%2==1:
        return "ODD"
    else:
        return "EVEN"
    
a=int(input("Enter a number:"))
print("Number",a,"is",eoro(a))