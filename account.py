# ---- VALIDATE LOGIN ---- #
import json
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Account:
    def create_account(self):
        new_name = input("Enter name to register: ").lower()
        new_password = input("Enter password to register: ")
        with open("accounts.json", "r", encoding="utf-8") as file:
                accounts = json.load(file)
        for i in range(len(accounts)):
            if new_name == accounts[i]["name"] and new_password == accounts[i]["password"]:
                clear()
                return print("User already registered!\n")
        for i in range(len(accounts)):
            model = {
                "name": new_name,
                "password": new_password
            }

            with open("accounts.json", "r", encoding="utf-8") as file:
                accounts = json.load(file)

            accounts.append(model)

            with open("accounts.json", "w", encoding="utf-8") as file:
                json.dump(accounts, file, indent=4, ensure_ascii=False)
            return print("Account created successfully!\n")

    def validate_account(self, name, password):
            with open("accounts.json", "r", encoding="utf-8") as file:
                accounts = json.load(file)
                for i in range(len(accounts)):
                    if accounts[i]["name"] == name and accounts[i]["password"] == password:
                        return True
    
    def login_account(self, name):
        password = input("Enter password: ")
        if Account.validate_account(self, name, password) == True:
            return True, print("- - - - - - - - - - - - - - -"), print(f"Welcome, {name}!\n")
        else: 
            return False
