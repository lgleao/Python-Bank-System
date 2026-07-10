from conta import Conta
from servicos import Servicos
import os

#Func de limpeza
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

#Classes
conta = Conta()
servico = Servicos()

while True:
# - - - Entrar na conta - - - #
    possui_conta = input("Já possui uma conta no banco? S/N\n").upper()
    #Função de cadastro
    if possui_conta == "N":
        print("- - - CADASTRO - - -")
        conta.criar_conta()
    #Função de login
    else:
        clear()
        print("- - - LOGIN - - -")
        nome = input("Digite nome: ").lower()
        if conta.login_conta(nome) == False:
            print("Login ou senha inválido(a), tente novamente!\n")
        else:
            clear()
            #Main loop
            while True:
                servico.opcoes()
                escolhas = int(input("Digite a opção desejada: "))
                
                #Transferir
                if escolhas == 1:
                    clear()
                    remetente = input("Digite o nome do remetente: ")
                    quantia = float(input("Quanto quer transferir: "))
                    clear()
                    servico.transferir(nome,remetente,quantia)
                #Sacar
                elif escolhas == 2:
                    clear()
                    saque = float(input("Quantidade a ser sacada: "))
                    servico.sacar(nome,saque)
                    print("Saque efetuado!\n")
                #Depositar
                elif escolhas == 3:
                    clear()
                    deposito = float(input("Quantidade a ser depositada: "))
                    servico.depositar(nome, deposito)
                    print("Quantia depositada!\n")
                #Mostrar saldo
                elif escolhas == 4:
                    clear()
                    servico.saldo(nome)
                #Encerrar app
                elif escolhas == 5:
                    clear()
                    servico.sair()