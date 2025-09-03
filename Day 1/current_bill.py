cname=input("Enetr the consumer name:")
cnum=input("Enter the consumer number:")
pmr=float(input("Enter the present month bill: "))
lmr=float(input("Enter last month bill: "))
tu=pmr-lmr
total=3.80*tu
print(f" Consumer name:{cname} \n consumer_number:{cnum} \n Present_month_bill:{pmr} \n last_month_bill:{lmr} \n bill:{total}")
