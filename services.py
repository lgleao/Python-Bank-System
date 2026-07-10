# ---- Bank Services ---- #

from account import Account
import json

class Services:
    def options(self):
        print("1. Transfer\n"
        "2. Withdraw\n"
        "3. Deposit\n"
        "4. Show balance\n"
        "5. Exit\n")

    def transfer(self, send, receive, amount):
        with open("accounts.json", "r", encoding="utf-8") as file:
            accounts = json.load(file)
        for i in range(len(accounts)):
            if send == receive:
                print("Invalid operation. User cannot make a deposit to themselves.")
            if accounts[i]["name"] == send:
                accounts[i]["balance"] = accounts[i]["balance"] - amount

            if accounts[i]["name"] == receive:
                accounts[i]["balance"] = accounts[i]["balance"] + amount
        print("Operation completed successfully!\n")
        
        with open("accounts.json", "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4, ensure_ascii=False)

    def withdraw(self, name, amount):
        with open("accounts.json", "r", encoding="utf-8") as file:
            accounts = json.load(file)
        if amount > 0:
            for i in range(len(accounts)):
                if accounts[i]["name"] == name:
                    accounts[i]["balance"] -= amount
                    with open("accounts.json", "w", encoding="utf-8") as file:
                        json.dump(accounts, file, indent=4, ensure_ascii=False)
                    return
        else:
            print("Invalid amount. Try another value.\n")

    def deposit(self, name, amount):
        with open("accounts.json", "r", encoding="utf-8") as file:
            accounts = json.load(file)
        if amount > 0:
            for i in range(len(accounts)):
                if accounts[i]["name"] == name:
                    accounts[i]["balance"] += amount
                    with open("accounts.json", "w", encoding="utf-8") as file:
                        json.dump(accounts, file, indent=4, ensure_ascii=False)
                    return
        else:
            print("Invalid amount. Try another value.\n")

    def balance(self, name):
        with open("accounts.json", "r", encoding="utf-8") as file:
            accounts = json.load(file)
        
        for i in range(len(accounts)):
            if accounts[i]["name"] == name:
                return print(f"Your current balance is: {accounts[i]["balance"]}")
            
        with open("accounts.json", "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4, ensure_ascii=False)

    def exit(self):
        print("Come back soon!")
        quit()
