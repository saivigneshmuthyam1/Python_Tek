def div_by_55(a):
    if a%55==0:
        return "Divisible by both 5 and 11"
    else:
        return "Not Divisible"
    
a=int(input("Enter a number:"))
print(div_by_55(a))