def digits_sum(a):
    sum =0;
    while(a>0):
        sum=sum+a%10
        a=a//10
    print(sum)

digits_sum(int(input("enter the number to find its digits sum")))
