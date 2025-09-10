def con(s):
    s1=s
    s1="".join(sorted(s1))
    ss=""
    count=1
    for i in range(1,len(s1)):
        if s1[i]==s1[i-1]:
            count=count+1
        else:
            ss=ss+s1[i-1]
            ss=ss+str(count)
            count=1
    ss += s1[i-1]+str(count)
    return ss




s=input("Enter the String: ").strip()
print(con(s))