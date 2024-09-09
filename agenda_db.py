from getkey import getkey, keys
clientes = []
id_cliente = [0]

def menu():
    print("\n                 |MENU|                 ")
    print("_________________________________________")
    print(" |1| - |Inserir Cliente|                 ")
    print(" |2| - |Listar Endereço do Cliente|      ")
    print(" |3| - |Deletar Cliente|                 ")
    print(" |4| - |Sair do Sistema|                 ")
    print("_________________________________________")

    opcao = int(input("Digite uma Opção: "))

    if opcao == 1:
        inserir_cliente()
    elif opcao == 2:
        listar_cliente()
    elif opcao == 3:
        deletar_cliente()
    elif opcao == 4:
        sair()
    else:
        print("Opção inválida! Digite uma opção correspondente ao |MENU|.")
        return menu()

def inserir_cliente():
    qtd_clientes = int(input("\nQuantos Clientes Deseja Cadastrar? "))

    for i in range(qtd_clientes):
        print("_________________________________")
        id = int(input("Digite o ID do(a) Cliente: "))
        nome = str(input("Digite o Nome do(a) Cliente: "))
        email = str(input("Digite o Email do(a) Cliente: "))
        telefone = str(input("Digite o Número de Telefone do(a) Cliente: "))
        registro = (id, nome, email, telefone)
        clientes.append(registro)
        
    print(" ")
    print(len(clientes), "Cliente(s) Adicionado(s)!")
    return menu()

def listar_cliente():

    if clientes == []:
        print("\nNenhum Cliente para exibir.")
        print("\nPressione |Enter| para Retornar ao Menu.")
        var = getkey()

        if var == keys.ENTER:
            return menu()
        else:
            print("Comando Inválido.")

    print("\n           |Lista de Cliente|            \n")
    
    for registro in clientes:
        print("|ID| ", registro[0], "|Nome| ", registro[1], "|Email| ", registro[2], "|Telefone| ", registro[3])
    
    
    print("\nPressione |Enter| para Retornar ao Menu.")
    var = getkey()

    if var == keys.ENTER:
        return menu()
    else:
        print("Comando Inválido.")
    

def deletar_cliente():

    if clientes == []:
        print("\nNenhum Cliente para Remover.")
        print("\nPressione |Enter| para Retornar ao Menu.")
        var = getkey()

    if var == keys.ENTER:
        return menu()
    else:
        print("Comando Inválido.")


    id_cliente = int(input("Digite o ID que deseja Deletar: "))

    for cliente in clientes:        
        if cliente[0] == id_cliente:
            clientes.remove(cliente)
            print(f"Cliente com ID {id_cliente} deletado com sucesso!")
            break
    
    return menu()

def sair():
    confirmacao = input("Tem certeza que deseja sair do sistema? Digite |s| para confirmar. ")

    if confirmacao.lower() == 's':
        print("\nSaindo do sistema...\n")
        quit()
    else:
        print("\nOpção Inválida.")
        print("\nVoltando para o |Menu|...")
    return menu()

if __name__ == "__main__":
    menu()