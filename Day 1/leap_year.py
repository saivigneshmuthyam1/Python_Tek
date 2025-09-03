def leap(a):
    if a%100==0 and a%400==0 and a%4!=0:
        return "NOT LEAP YEAR"
    else:
        return "LEAP YEAR"
    

a=int(input("Enter a year:"))
print("Year",a,"is",leap(a))