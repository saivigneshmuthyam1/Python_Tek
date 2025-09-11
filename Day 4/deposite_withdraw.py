class bankaccount:
    def __init__(self):
        self.__balance=0
    
    def deposite(self,amount):
        self.__balance=self.__balance+amount
        print("balance: ",self.__balance)
    
    def withdraw(self,amount):
        if amount <= self.__balance:
            print("Your Balance: ",self.__balance-amount)
        else:
            print("InSufficient Balance")
        
    def getbalance(self):
        print("Your Balance: ",self.__balance)

bank=bankaccount()
bank.deposite(3000)
bank.withdraw(1000)
bank.withdraw(4000)
bank.getbalance()
