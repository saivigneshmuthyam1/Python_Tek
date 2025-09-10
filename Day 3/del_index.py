def add(l,a):
    l.append(a)

def delete_index(l,a):
    l1=[]
    for i in range(len(l)):
        try:
            if i==a:
                continue
            else:
                l1.append(l[i])
        except :
            continue
    return l1



print("Enter the number of elemts to add in list")
n=int(input())
l=[]
for i in range(n):
    a=input("enter element to list : ")
    add(l,a)
a=int(input("enter index to remove"))
print(delete_index(l,a))