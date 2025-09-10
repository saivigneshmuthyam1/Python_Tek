def lenght(a):
    c=0
    for i in a:
        c=c+1
    return c

def comp(a,b):
    if a==b:
        print("Both String are equal")
    else:
        print("Not Equal")


a=input("Enter the string 1")
b=input("Enter the string 2")
print(f"Lenght of {a} :{lenght(a)}")
print(f"Lenght of {b} :{lenght(b)}")
print(a+b)
