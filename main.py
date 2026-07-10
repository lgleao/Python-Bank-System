from account import Account
from services import Services
import os

#Clear function
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

#Classes
account = Account()
service = Services()

while True:
# - - - Log into account - - - #
    has_account = input("Do you already have a bank account? Y/N\n").upper()
    #Registration function
    if has_account == "N":
        print("- - - REGISTRATION - - -")
        account.create_account()
    #Login function
    else:
        clear()
        print("- - - LOGIN - - -")
        name = input("Enter name: ").lower()
        if account.login_account(name) == False:
            print("Invalid login or password, try again!\n")
        else:
            clear()
            #Main loop
            while True:
                service.options()
                choice = int(input("Enter desired option: "))
                
                #Transfer
                if choice == 1:
                    clear()
                    sender = input("Enter the sender's name: ")
                    amount = float(input("How much do you want to transfer: "))
                    clear()
                    service.transfer(name,sender,amount)
                #Withdraw
                elif choice == 2:
                    clear()
                    withdrawal = float(input("Amount to withdraw: "))
                    service.withdraw(name,withdrawal)
                    print("Withdrawal completed!\n")
                #Deposit
                elif choice == 3:
                    clear()
                    deposit = float(input("Amount to deposit: "))
                    service.deposit(name, deposit)
                    print("Amount deposited!\n")
                #Show balance
                elif choice == 4:
                    clear()
                    service.balance(name)
                #Close app
                elif choice == 5:
                    clear()
                    service.exit()
