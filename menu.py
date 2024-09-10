from cliente_db import inserir_cliente, listar_cliente, deletar_cliente
from conexao import conecta_db

def menu_principal():
    print("\n                 |MENU|                 ")
    print("_________________________________________")
    print("       |1| - |Inserir Cliente|           ")
    print("       |2| - |Listar Cliente(s)|         ")
    print("       |3| - |Deletar Cliente|           ")
    print("       |4| - |Sair do Sistema|           ")
    print("_________________________________________")
    
    conexao = conecta_db()
    
    while True:
    

        opcao = input('\nEscolha Uma Opção: ')

        if opcao == "1":
            inserir_cliente(conexao)
        elif opcao == "2":
            listar_cliente(conexao)
        elif opcao == "3":
            deletar_cliente(conexao)
        elif opcao == "4":
            break
        else:
            print('Opção inválida! Tente novamente.')


if __name__ == "__main__":
    menu_principal()