def all_ocr(s,a):
    c=0
    for i in s:
        if i==a:
            c=c+1
    return c

s=input("Enter the String ")
a=input("Enter the character to search")
print(all_ocr(s,a))