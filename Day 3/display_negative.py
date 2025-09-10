def add(l,a):
    l.append(a)

def display_neg(l):
    for i in range(len(l)):
        try:
            num=int(l[i])
            if int(l[i])<0:
                print(l[i])
        except ValueError:
            continue



print("Enter the number of elemts to add in list")
n=int(input())
l=[]
for i in range(n):
    a=input("enter element to list : ")
    add(l,a)
display_neg(l)
