from typing import List


class Banking:
    def __init__(self, acc_no: int, name: str, account_type: str, branch: str):
        self.acc_no = acc_no
        self.name = name
        self.account_type = account_type
        self.branch = branch
        self.balance = 0
        
    def getbalance(self)->int:
        return self.balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"updated balance =  {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuff balance ")
            return
        self.balance-=amount
        print(f"updated balance ={self.balance}")
        
        
    def display(self):
        print(f"account number = {self.acc_no}")
        print(f"name  = {self.name}")
        print(f"account type = {self.account_type}")
        print(f"branch name = {self.branch} \n\n")
        print(f"balance = {self.balance}")


banks: List[Banking] = []
while True:
    print(" 1) add a acccount ")
    print("2) display all account")
    print("3) check balance of aaccount ")
    print("4) deposit balance ")
    print("5) withdraw ")
    print("6) Exit ")
    choice = int(input("enter the choice "))
    if choice == 1:
        acc_no = int(input("enter the account number = "))
        name = input("enter your name = ")
        account_type = input("enter choice your account type saving/current ")
        branch = input("enter brach name")
        x = Banking(acc_no, name, account_type, branch)
        banks.append(x)

    elif choice == 2:
        if len(banks) == 0:
            print("no user found")
        else:
            for i in banks:
                i.display()
    elif choice == 3:
        user_acount_no=int(input("enter the account number "))
        for acc in banks:
            if acc.acc_no==user_acount_no:
                print(f"your balance is = {acc.getbalance()}")
    elif choice==4:
        user_acount_no=int(input("enter the account number "))
        for acc in banks:
            if acc.acc_no==user_acount_no:  
                amount=int(input("enter the amount = "))
                acc.deposit(amount)    
                break
    elif choice==5:
        user_acount_no=int(input("enter the account number "))
        for acc in banks:
            if acc.acc_no==user_acount_no:  
                amount=int(input("enter the amount = "))
                acc.withdraw(amount)    
                break
    elif choice==6:
        break
    else:
        print("invailid choice ")
