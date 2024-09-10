from cliente_db import inserir_cliente, alterar_cliente, listar_cliente, deletar_cliente
from conexao import conecta_db

def menu_principal():
    print("\n                 |MENU|                 ")
    print("_________________________________________")
    print("       |1| - |Inserir Cliente|           ")
    print("       |2| - |Alterar Cliente|           ")
    print("       |3| - |Listar Cliente(s)|         ")
    print("       |4| - |Deletar Cliente|           ")
    print("       |5| - |Sair do Sistema|           ")
    print("_________________________________________")
    
    conexao = conecta_db()
    
    while True:
    

        opcao = input('\nEscolha Uma Opção: ')

        if opcao == "1":
            inserir_cliente(conexao)
        elif opcao == "2":
            alterar_cliente(conexao)
        elif opcao == "3":
            listar_cliente(conexao)
        elif opcao == "4":
            deletar_cliente(conexao)
        elif opcao == "5":
            print("Sistema Finalizado.")
            break
        else:
            print('Opção inválida! Tente novamente.')


if __name__ == "__main__":
    menu_principal()