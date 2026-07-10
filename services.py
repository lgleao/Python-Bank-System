# TO DO #
# ├── depositar()
# ├── sacar()
# ├── transferir()
# └── exibir_saldo()
from conta import Conta
import json

class Servicos:
    def opcoes(self):
        print("1. Transferir\n"
        "2. Sacar\n"
        "3. Depositar\n"
        "4. Exibir saldo\n"
        "5. Sair\n")

    def transferir(self, send, receive, amount):
        with open("contas.json", "r", encoding="utf-8") as arquivo:
            contas = json.load(arquivo)
        for i in range(len(contas)):
            if send == receive:
                print("Operação inválida. Usuário não pode efetuar depósito para si próprio.")
            if contas[i]["nome"] == send:
                contas[i]["saldo"] = contas[i]["saldo"] - amount

            if contas[i]["nome"] == receive:
                contas[i]["saldo"] = contas[i]["saldo"] + amount
        print("Operação efetuada com sucesso!\n")
        
        with open("contas.json", "w", encoding="utf-8") as arquivo:
            json.dump(contas, arquivo, indent=4, ensure_ascii=False)

    def sacar(self, nome, amount):
        with open("contas.json", "r", encoding="utf-8") as arquivo:
            contas = json.load(arquivo)
        if amount > 0:
            for i in range(len(contas)):
                if contas[i]["nome"] == nome:
                    contas[i]["saldo"] -= amount
                    with open("contas.json", "w", encoding="utf-8") as arquivo:
                        json.dump(contas, arquivo, indent=4, ensure_ascii=False)
                    return
        else:
            print("Quantia inválida. Tente outro valor.\n")

    def depositar(self, nome, amount):
        with open("contas.json", "r", encoding="utf-8") as arquivo:
            contas = json.load(arquivo)
        if amount > 0:
            for i in range(len(contas)):
                if contas[i]["nome"] == nome:
                    contas[i]["saldo"] += amount
                    with open("contas.json", "w", encoding="utf-8") as arquivo:
                        json.dump(contas, arquivo, indent=4, ensure_ascii=False)
                    return
        else:
            print("Quantia inválida. Tente outro valor.\n")

    def saldo(self, nome):
        with open("contas.json", "r", encoding="utf-8") as arquivo:
            contas = json.load(arquivo)
        
        for i in range(len(contas)):
            if contas[i]["nome"] == nome:
                return print(f"Seu saldo atual é de: {contas[i]["saldo"]}")
            
        with open("contas.json", "w", encoding="utf-8") as arquivo:
            json.dump(contas, arquivo, indent=4, ensure_ascii=False)

    def sair(self):
        print("Volte logo!")
        quit()