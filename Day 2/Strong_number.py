def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
    
def factn(n):
    for i in range(1,n+1):
        sum=0
        a=i
        while a>0:
            sum=sum+fact(a%10)
            a=a//10
        if sum==i:
            print(i)
             
    
x=int(input("enter the last number "))
factn(x)
