def sum_div(n):
    sum =0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum

def rang(n):
    for i in range(1,n+1):
        if sum_div(i)==i:
            print(i)

rang(int(input("Enter the range: ")))