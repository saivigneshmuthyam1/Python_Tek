def count(s):
    ap=al=dig=0
    for i in s:
        if i.isdigit():
            dig=dig+1
        elif i.isalpha():
            ap=ap+1
        else:
            al=al+1
    print(f"Count of Digits:{dig}\nCount of Alphabets:{ap}\nCount of Special char:{al}\n")

a=input("Enter the String: ")
count(a)