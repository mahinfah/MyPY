print("welcome to the Bank")

class account:
     def __init__(self,name,balance,pin):   
         self.name=name
         self.balance=0
         self.pin=0

     @staticmethod
     def rules():
       print("1. You can deposit money")
       print("2. You can withdraw money")
       print("3. You can check balance")
        
     def deposit(self,amount):
            self.balance+=amount
            print("Amount Deposited")   
     def withdraw(self,amount):
            if self.balance>=amount:
                self.balance-=amount
                print("Amount Withdrawn")
            else:
                print("Insufficient Balance")      
     def display(self):
            print("Name:",self.name)
            print("Balance:",self.balance)
            print("Pin:",self.pin)


person1=account("John",0,0)
person1.rules()
person2=account("Smith",0,0)
person1.deposit(1000)
person1.withdraw(5000)
person1.withdraw(500)
person1.display()









