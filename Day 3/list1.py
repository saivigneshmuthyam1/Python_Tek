def add(l,a):
    l.append(a)

print("Enter the number of elemts to add in list")
n=int(input())
l=[]
for i in range(n):
    a=input("enter element to list : ")
    add(l,a)
print(l)