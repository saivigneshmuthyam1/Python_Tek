def add(l,a):
    l.append(a)

def second_lar_sort(l):
    l.sort()
    print(l[-2])

#def second_lar(l):


print("Enter the number of elemts to add in list")
n=int(input())
l=[]
for i in range(n):
    a=int(input("enter element to list : "))
    add(l,a)
second_lar_sort(l)