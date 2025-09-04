name=input("Enter Name of Student:")
roll=input("Enter the Roll number of Student:")
s1=float(input("Enter subject 1 Marks:"))
s2=float(input("Enter subject 2 Marks:"))
s3=float(input("Enter subject 3 Marks:"))
avg=round(((s1+s2+s3)/3),2)
print(f" Name:{name} \n Roll_number:{roll} \n Subject 1 marks:{s1} \n Subject 2 marks:{s2} \n Subject 3 marks:{s3} \n Average:{avg}")
if avg>=40 and s1>=40 and s2>= 40 and s3>=40:
    if(avg<=50):
        print("Grade is: C")
    elif(51<=avg<=70):
        print("Grade is : B")
    elif(71<=avg<=80):
        print("Grade is : A" )
    elif(81<=avg<=100):
        print("Grade is : S")
    else:
        print("Wrong input of marks")

else:
    print("FAIL")

    
