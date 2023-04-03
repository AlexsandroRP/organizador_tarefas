import mysql.connector


meubd = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'admin',
    database = 'Tarefas'
)

# Criar cursor
cursor = meubd.cursor()


# FUNÇÕES

# ADD Tarefa ao DB
def add_tarefas(i):
    sql = "INSERT INTO tarefas (descricao, concluidO) VALUES (%s, %s)"
    dados = (i, False)
    cursor.execute(sql, dados)
    meubd.commit()

# OBTER TODAS AS TAREFAS
def get_tarefas():
    sql = "SELECT * FROM tarefas"
    cursor.execute(sql)
    return cursor.fetchall()
    
print(get_tarefas())

# MARCAR CASO TAREFA JÁ FOI CONCLUÍDA
def tarefa_concluida(id_tarefa):
    sql = ("UPDATE tarefas SET concluido = True WHERE id = %s")
    dados = (id_tarefa,) #sempre colocar virgula para o sql entender coomo lista ou tupla, senão vai dar erro   
    cursor.execute(sql, dados)
    meubd.commit()
    
#tarefa_concluida(1) # marca a tarefa do id como True   


# DELETAR TAREFAS NO DB
def deletar_tarefa(id_tarefa):
    sql = ("DELETE FROM tarefas WHERE id = %s")
    dados = (id_tarefa,)
    cursor.execute(sql, dados)
    meubd.commit()
    
#deletar_tarefa(1)  


# INTERAGINDO COM AS FUNCIONALIDADES


