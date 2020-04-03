import sqlite3

conn = sqlite3.connect('teste.db')
# conn.execute('create table Aluno(ID integer, nome text)')
conn.execute('insert into Aluno values (1, "Oseias")')
conn.execute('insert into Aluno values (2, "Guilherme")')
conn.execute('insert into Aluno values (3, "Juliano")')

for row in conn.execute('select * from Aluno order by nome'):
    print(row)
