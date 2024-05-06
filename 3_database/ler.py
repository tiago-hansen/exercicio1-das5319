import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def read_from_db():
    print("[Lendo toda a base de dados]")
    c.execute('SELECT * FROM Alunos')
    data = c.fetchall()
    for row in data:
        print(row)

    print("\n[Quem trancou o curso?]")
    c.execute('SELECT * FROM Alunos WHERE Situacao = "Trancamento"')
    data = c.fetchall()
    for row in data:
        print(row)

    print("\n[Quem entrou após 2012?]")
    c.execute('SELECT * FROM Alunos WHERE Ingresso > 2012')
    data = c.fetchall()
    for row in data:
        print(row)

    print("\n[Qual a idade de Patrick?]")
    c.execute('SELECT Idade FROM Alunos WHERE Nome = "Patrick"')
    data = c.fetchall()
    for row in data:
        print(row)

    print("\n[Alterando o nome de Pedro para Carlos...]")
    c.execute('UPDATE Alunos SET Nome = "Carlos" WHERE Nome = "Pedro"')
    print("[Lendo a base de dados após a alteração]")
    c.execute('SELECT * FROM Alunos')
    data = c.fetchall()
    for row in data:
        print(row)

read_from_db()
c.close()
conn.close()