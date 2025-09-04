def arm(n):
    a=n
    sum=0
    while a>0:
        x=a%10
        sum=sum+(pow(x,3))
        a=a//10
    if sum==n:
        print(n)

def armm(n):
    for i in range(n+1):
        arm(i)

armm(int(input("Enter the range to test ")))

