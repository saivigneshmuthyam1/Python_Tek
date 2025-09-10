def Add(t):
    t1=()
    Name=input("Enter The Name of Student").strip()
    rol=input("Enter The Roll Number of Student".strip())
    m=int(input("Enter the marks of Student"))
    t1=(Name,rol,m)
    return t+(t1,)

def Highest(t):
    x=-1
    q=0
    for i in range(0,len(t)):
        if x<t[i][2]:
            q=i
            x=t[i][2]
    print(t[q])

a=int(input("Enter the NUmber of Studenrts:"))
t=()
for i in range(a):
   t= Add(t)
Highest(t)