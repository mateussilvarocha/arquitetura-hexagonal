import mysql.connector
from mysql.connector import Error
from manipulador.security import LoginSQL
from cryptography.fernet import Fernet

# Gerar uma chave para criptografia
key = Fernet.generate_key()

login = LoginSQL(key)

host_name = login.host_name 
user_name = login.user_name
pw = login.user_password

bd= 'mundo'

#-------------  Functions ---------------

def conexao_server(host_name, user_name, user_password):
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database sucesso a conexao ")
    except Error as err:
        print(f"Error: '{err}'")

    return conexao



def conexao_nomebd(host_name, user_name, user_password, db_name):
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database conexao successful")
    except Error as err:
        print(f"Error: '{err}'")

    return conexao


def criar_bd(conexao, query):
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        print("Database criado com sucesso")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(conexao, query):
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        conexao.commit()
        print("Sucesso na manipulaçao da query")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(conexao, query):
    
    cursor = conexao.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
    
# def get_id(conexao):
#     query = "SELECT pessoa_id FROM pessoa ORDER BY pessoa_id ASC;"
#     cursor = conexao.cursor()
#     try:
#         cursor.execute(query)
#         ids_ocupados = cursor.fetchall()
#         ids_ocupados = [id[0] for id in ids_ocupados]  # Converter de tuplas para lista de IDs

#         # Encontrar o menor ID disponível a partir do 1
#         proximo_id = 1
#         while proximo_id in ids_ocupados:
#             proximo_id += 1

#         return proximo_id
#     except Error as err:
#         print(f"Error: '{err}'")
#     finally:
#         cursor.close()





# #---------------  Tabelas  ------------------

# conexao = conexao_nomebd(host_name, user_name, pw, bd)

# def criar_tabela_pessoa(nome, idade):
#     #recebe o id do ultimo criado
#     criar_tabela_pessoa = f'CREATE TABLE pessoa (1 INT PRIMARY KEY, {nome} VARCHAR(40) NOT NULL, {idade} INT);'

#     execute_query(conexao, criar_tabela_pessoa)

# def criar_tabela_partecorpo(lista_partes):
#     #recebe o id do ultimo criado
#     criar_tabela_pessoa = f'CREATE TABLE partecorpo (1 INT PRIMARY KEY, {nome} VARCHAR(40) NOT NULL, {idade} INT);'

#     execute_query(conexao, criar_tabela_pessoa)

# def criar_tabela_inventario(lista_itens):
#     #recebe o id do ultimo criado
#     criar_tabela_pessoa = f'CREATE TABLE itens (1 INT PRIMARY KEY, {nome} VARCHAR(40) NOT NULL, {idade} INT);'

#     execute_query(conexao, criar_tabela_pessoa)
# def adiciona_pessoa(nome, idade):
    
#     id = get_id(conexao)
#     print(id)#none
#     pessoa = f'INSERT INTO pessoa (pessoa_id, nome, idade) VALUES ({id}, "{nome}", {idade});'

#     execute_query(conexao, pessoa)

# def update(id, nome, idade):
#  #identifica pelo id e muda o nome a idade
#     update= f'UPDATE pessoa SET nome = "{nome}", idade = {idade} WHERE pessoa_id = {id};'
#     execute_query(conexao, update)

# def delete(conexao, id):
#     query = f'DELETE FROM pessoa WHERE pessoa_id = {id};'
#     cursor = conexao.cursor()
#     try:
#         cursor.execute(query)
#         conexao.commit()  # Faz o commit da operação
#         print(f"Registro com pessoa_id = {id} deletado com sucesso.")
#     except Error as err:
#         print(f"Error: '{err}'")
#     finally:
#         cursor.close()


# def print_query(results):
#     for result in results:
#         print(result)

# query = """
#     SELECT *
#     FROM pessoa;
#     """
# results = read_query(conexao, query)

# print_query(results)

# delete(conexao, 1)
# update(3, 'mateus', 22)

# print_query(results)
# adiciona_pessoa("Carlos", 30)

# print_query(results)

# from_db = []

# # Percorrer os resultados e inseri-los à lista

# # Retorna uma lista de tuplas
# for result in results:
#     result = result
#     from_db.append(result)

