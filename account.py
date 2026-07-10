# ---- VALIDAR LOGIN ---- #
import json
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Conta:
    def criar_conta(self):
        novo_nome = input("Digite nome a ser cadastrado: ").lower()
        nova_senha = input("Digite senha a ser cadastrada: ")
        with open("contas.json", "r", encoding="utf-8") as arquivo:
                conta = json.load(arquivo)
        for i in range(len(conta)):
            if novo_nome == conta[i]["nome"] and nova_senha == conta[i]["senha"]:
                clear()
                return print("Usuário já cadastrado!\n")
        for i in range(len(conta)):
            model = {
                "nome": novo_nome,
                "senha": nova_senha
            }

            with open("contas.json", "r", encoding="utf-8") as arquivo:
                contas = json.load(arquivo)

            contas.append(model)

            with open("contas.json", "w", encoding="utf-8") as arquivo:
                json.dump(contas, arquivo, indent=4, ensure_ascii=False)
            return print("Conta criada com sucesso!\n")

    def valida_conta(self, name, password):
            with open("contas.json", "r", encoding="utf-8") as arquivo:
                conta = json.load(arquivo)
                for i in range(len(conta)):
                    if conta[i]["nome"] == name and conta[i]["senha"] == password:
                        return True
    
    def login_conta(self, nome):
        senha = input("Digite senha: ")
        if Conta.valida_conta(self, nome, senha) == True:
            return True, print("- - - - - - - - - - - - - - -"), print(f"Seja bem-vindo, {nome}!\n")
        else: 
            return False

# SINTAXE #      
# conta = Conta()
# conta.login_conta()
# conta.criar_conta()
# conta.valida_conta()