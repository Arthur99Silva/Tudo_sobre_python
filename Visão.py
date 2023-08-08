from persistencia import Persistente
from entidade import Entidade, Cliente, Conta, Transacao
import sys

class Visao:
    def __init__(self):
        self.bd = Persistente()
    
    def mostrar_menu(self):
        while True:
            print("== Menu ==")
            print("1. Cliente")
            print("2. Conta")
            print("3. Transação")
            print("0. Sair")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                self.menu_cliente()
            elif opcao == "2":
                self.menu_conta()
            elif opcao == "3":
                self.menu_transacao()
            elif opcao == "0":
                print("Saindo...")
                sys.exit()
            else:
                print("Opção inválida")
    
    def menu_cliente(self):
        while True:
            print("== Menu Cliente ==")
            print("1. Inserir")
            print("2. Alterar")
            print("3. Excluir")
            print("4. Buscar por id")
            print("0. Voltar")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                nome = input("Digite o nome do cliente: ")
                endereco = input("Digite o endereço do cliente: ")
                self.bd.inserir_cliente(Cliente(nome, endereco))
            elif opcao == "2":
                id = input("Digite o id do cliente a ser alterado: ")
                nome = input("Digite o novo nome do cliente: ")
                endereco = input("Digite o novo endereço do cliente: ")
                self.bd.alterar_cliente(id, Cliente(nome, endereco, id))
            elif opcao == "3":
                id = input("Digite o id do cliente a ser excluído: ")
                self.bd.excluir_cliente(id)
            elif opcao == "4":
                id = input("Digite o id do cliente a ser buscado: ")
                cliente = self.bd.buscar_cliente(id)
                if cliente:
                    print(cliente)
                else:
                    print("Cliente não encontrado")
            elif opcao == "0":
                break
            else:
                print("Opção inválida")
    
    def menu_conta(self):
        while True:
            print("== Menu Conta ==")
            print("1. Inserir")
            print("2. Alterar")
            print("3. Excluir")
            print("4. Buscar por id")
            print("0. Voltar")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                numero = input("Digite o número da conta: ")
                titular = input("Digite o nome do titular da conta: ")
                self.bd.inserir_conta(Conta(numero, titular))
            elif opcao == "2":
                id = input("Digite o id da conta a ser alterada: ")
                numero = input("Digite o novo número da conta: ")
                titular = input("Digite o novo nome do titular da conta: ")
                self.bd.alterar_conta(id, Conta(numero, titular, id))
            elif opcao == "3":
                id = input("Digite o id da conta a ser excluída: ")
                self.bd.excluir_conta(id)
            elif opcao == "4":
                id = input("Digite o id da conta a ser buscada: ")
                conta = self.bd