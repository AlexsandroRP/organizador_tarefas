import mysql.connector


meubd = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'admin',
    database = 'Tarefas'
)

# Criar DB
cursor = meubd.cursor()
#cursor.execute("CREATE DATABASE Tarefas")

# CRIANDO TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS tarefas(id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(255), concluido BOOLEAN)")




