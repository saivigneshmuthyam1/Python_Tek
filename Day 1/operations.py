def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    if b==0:
        return "b is zero "
    else:
        return a/b
    
def mul(a,b):
    return a*b

def fd(a,b):
    if b==0:
        return "b is zero"
    else:
        return a//b
    
a,b=map(int,input("Enter a,b").split())
print("Addation: ",sum(a,b))
print("Subraction: ",sub(a,b))
print("Multiplication: " ,mul(a,b))
print("Division: ",div(a,b))
print("Floor Division: ",fd(a,b))