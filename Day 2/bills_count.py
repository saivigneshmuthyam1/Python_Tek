def count(a):
    n=a
    print("Number of 500 bills",n//500)
    n=n%500
    print("Number of 200 bills",n//200)
    n=n%200
    print("Number of 100 bills",n//100)
    n=n%100
    print("NUmber of 50 Bills",n//50)
    n=n%50
    print("Number of 20 bills",n//20)
    n=n%20
    print("Number of 10 bills",n//10)
    n=n%10
    print("NUmber of 5 bills",n//5)
    n=n%5
    print("NUmber of 2 bills",n//2)
    n=n%2
    print("Number of 1 bills",n)

a=int(input("Enter the amount to get least number of bills:"))
count(a)