import mysql.connector
from mysql.connector import Error


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

pw = '1234'
bd= 'mundo'
conexao = conexao_server("localhost", "root", pw)
criar_bd(conexao, f'CREATE DATABASE {bd}')

def delete(conexao, id):
    query = f'DELETE FROM pessoa WHERE pessoa_id = {id};'
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        conexao.commit()  # Faz o commit da operação
        print(f"Registro com pessoa_id = {id} deletado com sucesso.")
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()


#---------------  Tabelas  ------------------

criar_tabela_pessoa = """
CREATE TABLE pessoa (
  pessoa_id INT PRIMARY KEY,
  nome VARCHAR(40) NOT NULL,
  idade INT 
  );
 """

pop_teacher = """
INSERT INTO pessoa VALUES
(1,  'James', 11),
(2, 'Stefanie',  11), 
(3, 'Steve', 11),
(4, 'Friederike', 11),
(5, 'Isobel', 11),
(6, 'Niamh', 11);
"""

update = """
UPDATE pessoa
SET nome = 'Mateus' 
WHERE pessoa_id = 2;
"""


conexao = conexao_nomebd("localhost", "root", pw, bd) # Connect to the Database
execute_query(conexao, criar_tabela_pessoa) # Execute our defined query
execute_query(conexao, pop_teacher)
q1 = """
SELECT *
FROM pessoa;
"""

results = read_query(conexao, q1)
for result in results:
  print(result)

delete(conexao, 1)
execute_query(conexao, update)

results = read_query(conexao, q1)
for result in results:
  print(result)
from_db = []

# Percorrer os resultados e inseri-los à lista

# Retorna uma lista de tuplas
for result in results:
  result = result
  from_db.append(result)

