import sqlite3

conn = sqlite3.connect("Usuarios.db")

cursor = conn.cursor()

def cria_tabela():
    sql = """
    CREATE TABLE IF NOT EXISTS endereco(
        CEP CHAR(8),
        Logradouro VARCHAR(120),
        Número VARCHAR(15),
        Complemento VARCHAR(50),
        Bairro VARCHAR(40),
        Localidade VARCHAR(40),
        UF CHAR(2),
        IBGE VARCHAR(15),
        gia VARCHAR(15),
        DDD VARCHAR(3),
        SIAFI VARCHAR(15)
    )
    """
    cursor.execute(sql)

    conn.commit()

def adiciona_cep(dic_requisicao, numero):
    cria_tabela()

    cep = dic_requisicao['cep']
    logradouro = dic_requisicao['logradouro']
    complemento = dic_requisicao['complemento']
    bairro = dic_requisicao['bairro']
    localidade = dic_requisicao['localidade']
    uf = dic_requisicao['uf']
    ibge = dic_requisicao['ibge']
    gia = dic_requisicao['gia']
    ddd = dic_requisicao['ddd']
    siafi = dic_requisicao['siafi']

    cursor.execute(f"INSERT INTO endereco VALUES(?,?,?,?,?,?,?,?,?,?,?)", (cep, logradouro, numero, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi))

    conn.commit()
