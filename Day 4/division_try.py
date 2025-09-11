a,b=map(int,input("Enter the divisior and divident: ").split())
try:
    print(a/b)
except ZeroDivisionError:
    print("Error:Division by Zero is not allowed")
else:
    print("Successfully Executed")
finally:
    print("-"*30)

