def greater(a,b,c):
    if a>b:
        if a>c:
            print("a is greater")
        else:
            print("c is greater")
    elif b>c:
        print("b is greater")
    else:
        print("c is greater")

a,b,c=map(int,input("Enter a,b,c").split())
greater(a,b,c)