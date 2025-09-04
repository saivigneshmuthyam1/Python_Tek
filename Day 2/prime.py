def prime(a):
    count=2
    for i in  range(2,a):
        if(a%i==0):
            count=count+1
    if count!=2:
        print("Not Prime")
    else:
        print("Prime")

prime(int(input("Enter number to check prime or not ")))