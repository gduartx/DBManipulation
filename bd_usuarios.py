import sqlite3
import format
import cep as c
import bd_cep as bd
conn = sqlite3.connect("Usuarios.db")

cursor = conn.cursor()

def criar_tabela():
    bd.cria_tabela()

    sql = """
    CREATE TABLE IF NOT EXISTS Usuario(
        id_usuario INTEGER IDENTITY,
        username VARCHAR(50),
        nome VARCHAR(50),
        sobrenome VARCHAR(50),
        cpf VARCHAR(15),
        data_nascimento DATETIME,
        cep CHAR(8),
        email VARCHAR(100),

        Constraint PK_pessoa PRIMARY KEY (id_usuario),
        Constraint UQ_pessoa_cpf UNIQUE (cpf),
        Constraint UQ_pessoa_username UNIQUE (username),
        Constraint UQ_pessoa_email UNIQUE (email)
        Constraint FK_pessoa_endereco FOREIGN KEY cpf REFERENCES endereco(cpf)
    )    
    """

    cursor.execute(sql)

    conn.commit()
def verifica_user(username):
    sql = "SELECT username FROM Usuario"
    cursor.execute(sql)

    while username in cursor.fetchall():
        username = input('Username já em uso, digite outro: ')

def adiciona_pessoa():
    criar_tabela()
    username = input('Username: ')
    verifica_user(username)
    nome = input('Nome: ')
    nomef = nome
    nome = format.formata_nome(nomef)
    sobrenome = input('Sobrenome: ')
    nomef = sobrenome
    sobrenome = format.formata_nome(nomef)
    cpf = (input('CPF: '))
    cpf_format = format.formata_cpf(cpf)
    data = input('Data de Nascimento: ')
    cep = input('CEP: ')
    cep = c.formata_cep(cep)
    c.add_cep(cep)
    email = input('Email: ')
    id = None
    cursor.execute("INSERT INTO Usuario VALUES(?,?,?,?,?,?,?,?)", (id, username, nome, sobrenome, cpf_format, data, cep, email))

    conn.commit()

def deleta_pessoa():
    consulta_pessoa()
    id = int(input("""
==============================================
            DELEÇÃO DE CADASTRO
==============================================
Digite o ID que será deletado
    """))
    cursor.execute("DELETE FROM Usuario WHERE id_usuario = (?)", (id,))

    conn.commit()


def consulta_pessoa():
    sql = """
        SELECT * FROM usuario
    """
    cursor.execute(sql)
    count = 0
    for row in cursor.fetchall():
        count += 1
        id, username, nome, sobrenome, cpf, data, cep, email = row
        print(f"""
        {count}º Pessoa
        Id = {id}
        Username = {username}
        Nome Completo = {nome + ' ' + sobrenome}     
        CPF = {cpf}
        Data de Nascimento = {data}
        CEP = {cep}
        Email = {email}
        """)

def atualizar_cadastro():
    consulta_pessoa()
    dado = int(input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite o ID de quem será atualizado
    """))
    
    att = int(input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Escolha qual dado será atualizado
[1] - Nome
[2] - Sobrenome
[3] - CPF
[4] - Data de Nascimento
[5] - Username
[6] - Email
==============================================
"""))
    if att == 1:

        novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite qual será o novo nome:""")
        print('Nome atualizado')

        cursor.execute("""UPDATE Usuario 
                          SET nome = (?) 
                          WHERE id_usuario = (?);""", (novo_dado, dado))
    elif att == 2:

        novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite qual será o novo sobrenome:""")

        cursor.execute("""UPDATE Usuario
                          SET sobrenome = (?) 
                          WHERE id_usuario = (?);""", (novo_dado, dado))
        print('Sobrenome atualizado')

    elif att == 3:

        novo_dado = int(input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite qual será o novo CPF:"""))

        cursor.execute("""UPDATE Usuario 
                          SET cpf = (?) 
                          WHERE id_usuario = (?);""", (novo_dado, dado))
        print('CPF atualizado')

    elif att == 4:
        
        novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite qual será a nova data de nascimento:""")

        cursor.execute("""UPDATE Usuario
                          SET data_nascimento = (?) 
                          WHERE id_usuario = (?);""", (novo_dado, dado))
        print('Data de nascimento atualizada')

    elif att == 5:
        
        novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite qual será o novo username: """)

        cursor.execute("""
            SELECT username FROM Usuario
        """)
        for row in cursor.fetchall:
            if row == novo_dado:
                while row == novo_dado:
                    novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Username já em uso, digite outro: """)


        cursor.execute("""UPDATE Usuario
                          SET username = (?) 
                          WHERE id_usuario = (?);""", (novo_dado, dado))
        print('Username atualizado')

    elif att == 6:
        
        novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite qual será o novo email: """)

        cursor.execute("""
            SELECT email FROM Usuario
        """)
        for row in cursor.fetchall:
            if row == novo_dado:
                while row == novo_dado:
                    novo_dado = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Email já em uso, digite outro: """)


        cursor.execute("""UPDATE Usuario
                          SET email = (?) 
                          WHERE id_usuario = (?);""", (novo_dado, dado))
        print('Email atualizado')


def consulta_endereco():
    consulta_pessoa()
    id = input("""
==============================================
            ATUALIZAÇÃO DE CADASTRO
==============================================
Digite o id do usuario a qual o endereco será consultado: """)

    cursor.execute("""
        SELECT u.cep, u.id_usuario, e.cep, e.logradouro, e.Número, e.Complemento, e.bairro, e.Localidade, e.UF
        FROM Usuario as u JOIN endereco as e
        ON u.cep = e.CEP
        WHERE u.id_usuario = (?)
        """, (id,))

    print(cursor.fetchall())
    print(cursor.fetchmany())
    print(cursor.fetchone())
    for row in cursor.fetchall():
        print(row, 'AOBA')



conn.commit()

