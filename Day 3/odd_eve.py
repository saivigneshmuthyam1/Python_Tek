def add(l,a):
    l.append(a)

def count(l):
    odd=eve=0
    for i in range(len(l)):
            if l[i]<0:
                odd=odd+1
            elif l[i]==0:
                 neu=neu+1
            else:
                 eve=eve+1
    print(f"Even:{eve} \n odd:{odd} \n zeros:{neu}")


print("Enter the number of elemts to add in list")
n=int(input())
l=[]
for i in range(n):
    a=int(input("enter element to list : "))
    add(l,a)
count(l)
