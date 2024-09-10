
def inserir_cliente(conexao):
    cursor = conexao.cursor()
    nome = (input("Digite o Nome do(a) Cliente: "))
    email = (input("Digite o Email do(a) Cliente: "))
    telefone = (input("Digite o Número de Telefone do(a) Cliente: "))

    sql_insert = "insert into cliente (nome, email, telefone) values ( %s, %s, %s)"
    registro = (nome, email, telefone)
    cursor.execute(sql_insert, registro)
    conexao.commit()
    print("Cliente Cadastrado com Sucesso!")

def alterar_cliente(conexao):
    cursor = conexao.cursor()
    id =   input("Digite o ID que deseja alterar: ")
    nome = input("Digite o novo nome: ")
    email = input("Digite o novo email: ")
    telefone = input("Digite o novo telefone: ")

    sql_update = "update cliente set nome = %s, email = %s, telefone = %s where id = %s"
    dados = (nome, email, telefone, id)
    cursor.execute(sql_update, dados)
    conexao.commit()
    print("Cliente alterado com sucesso!")

def listar_cliente(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id, nome, email, telefone from cliente")
    registros = cursor.fetchall()

    print("\n|Lista de Cliente|\n")
    
    for registro in registros:
        print("|ID| ", registro[0], "|Nome| ", registro[1], "|Email| ", registro[2], "|Telefone| ", registro[3])

def deletar_cliente(conexao):
    cursor = conexao.cursor()
    id = (input("Digite o ID que deseja Deletar: "))
        
    sql_delete = "delete from cliente where id =" + id
    cursor.execute(sql_delete)
    conexao.commit()

    print(f"Cliente com ID {id} deletado com sucesso!")
