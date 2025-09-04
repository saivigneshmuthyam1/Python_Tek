def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
a=int(input("Enter the range: "))
for i in range(a):
    print(fibo(i),end=" ")