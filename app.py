import mysql.connector


meubd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bancodedados'
)

# criando o db
cursor = meubd.cursor()
cursor.execute("SHOW DATABASES LIKE'crud'")

resultado = cursor.fetchone() # caso não encontre nenhuma linha, retorna NONE

if resultado:
    print('O banco de dados já existe!')
else:
    print('O banco de dados ainda não existe.')   
    cursor.execute("CREATE DATABASE crud")
    
    
# OPERAÇÕES CRUD
# CREATE
#cursor.execute("CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))")    

'''# INSERINDO DADOS
sql = "INSERT INTO clientes (nome, email) VALUES (%s,%s)"
dados = ("Zé", "Zé@teste.com")
cursor.execute(sql, dados)

#Fazendo coommit
meubd.commit()'''



# LER REGISTROS NO DB
# READ
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall() # retorna todos os resultados do comando acima

for i in resultado:
    print(i)
    
    
    
# UPDATE
'''sql = "UPDATE clientes SET nome=%s WHERE nome =%s"
dados = ("Zé Update", "Zé") # troca o zé pelo zé update   

cursor.execute(sql, dados)
meubd.commit()'''



# DELETE
'''sql = "DELETE FROM clientes WHERE nome =%s"
dados = (["Alex"])
cursor.execute(sql, dados)
meubd.commit()
    '''
    
    

