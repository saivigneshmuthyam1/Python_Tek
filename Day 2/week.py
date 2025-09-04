def week(a):
    if(a==1):
        print("Monday")
    elif(a==2):
        print("Tuesday")
    elif a==3:
        print("wednesday")
    elif a==4:
        print("Thursday")
    elif a==5:
        print("Friday")
    elif a==6:
        print("Saturday")
    elif a==0:
        print("Sunday")
    else:
        print("Invalid Input")

a=int(input("Enter week number(0-6)"))
week(a)