class Bankaccount:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            print("Deposit a positive number")
        else:
            self.balance += amount
            print("Your current amount is:",self.balance)
    def withdraw(self,amount):
        if amount >= self.balance:
           print("Insufficient balance")
        elif amount <= 0:
            print("Enter a positive number")
        else:
            self.balance -= amount
            print("Your current balance is:",self.balance)
    def display(self):
        print("Account Number:",self.acc_no)
        print("Name:",self.name)
        print("Account Type:",self.acc_type)
        print("Balance:",self.balance)
no=int(input("Enter Account Number:"))
name=input("Enter Your Name:")
type=input("Enter Account Type:")
bal=int(input("Enter Current Balance:"))
user1=Bankaccount(no,name,type,bal)
while True:
    print("\n1.Deposit\n2.Withdraw\n3.Account Details\n4.Exit\n")
    opt=int(input("enter the option"))
    if opt==1:
        amount=int(input("enter your deposit amount"))
        user1.deposit(amount)
    elif opt==2:
        amount=int(input("enter your withdrawal amount"))
        user1.withdraw(amount)
    elif opt==3:
        user1.display()
    elif opt==4:
        exit(0)
    else:
        print("invalid option")

