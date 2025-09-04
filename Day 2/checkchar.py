def check(a):
    if a.isalpha():
        print("This is Alphabet")
    elif a.isdigit():
        print("This is number")
    else:
        print("Other characters")

a=input("Enter a character or number")
check(a)
