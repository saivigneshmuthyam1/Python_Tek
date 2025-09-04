def lop(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()

lop(int(input("Enter length:")))