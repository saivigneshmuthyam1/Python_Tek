def all_ocr(s,a):
    c=-1
    for i in s:
        c=c+1
        if i==a:
            print(c,end=" ")

s=input("Enter the String ")
a=input("Enter the character to search")
all_ocr(s,a)