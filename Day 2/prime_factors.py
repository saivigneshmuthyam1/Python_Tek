def fact(n):
    for i in range(1,n+1):
        if n%i==0:
            isprime(i)

def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print(n)

fact(int(input("Enter Number to find factors: ")))