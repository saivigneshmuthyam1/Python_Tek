cname=input("Enetr the consumer name:")
cnum=input("Enter the consumer number:")
pmr=float(input("Enter the present month bill: "))
lmr=float(input("Enter last month bill: "))
tu=pmr-lmr
#total=3.80*tu
if(0<=tu<=50):
    total=tu*3.80
elif(51<=tu<=100):
    total=(50*3.80)+((tu-50)*4.20)
elif(101<=tu<=200):
    total=(50*3.80)+((50)*4.20)+((tu-100)*5.10)
elif(201<=tu<=300):
    total=(50*3.80)+((50)*4.20)+(100*5.10)+((tu-200)*6.30)
else:
    total=(50*3.80)+((50)*4.20)+(100*5.10)+(100*6.30)+((tu-300)*7.50)
print(f" Consumer name:{cname} \n consumer_number:{cnum} \n Present_month_bill:{pmr} \n last_month_bill:{lmr} \n bill:{total}")
