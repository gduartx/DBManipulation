import bd_usuarios

#bd_usuarios.criar_tabela()

x = int(input("""
==============================================
                MENU PRINCIPAL
==============================================
[1] - Consultar usuários cadastrados
[2] - Cadastrar usuário
[3] - Deletar cadastro
[4] - Atualizar cadastro
[5] - Consultar endereços cadastrados
[6] - Fechar sistema
==============================================
"""))

if x == 1:
    bd_usuarios.consulta_pessoa()
elif x == 2:
    bd_usuarios.adiciona_pessoa()
elif x == 3:
    bd_usuarios.deleta_pessoa()
elif x == 4:
    bd_usuarios.atualizar_cadastro()
elif x == 5:
    bd_usuarios.consulta_endereco()

while x != 6:
    x = int(input("""
==============================================
                MENU PRINCIPAL
==============================================
[1] - Consultar pessoas cadastradas
[2] - Cadastrar pessoa
[3] - Deletar cadastro pelo nome
[4] - Atualizar cadastro
[5] - Consultar endereços cadastrados
[6] - Fechar sistema
==============================================
"""))
    if x == 1:
        bd_usuarios.consulta_pessoa()
    elif x == 2:
        bd_usuarios.adiciona_pessoa()
    elif x == 3:
        bd_usuarios.deleta_pessoa()
    elif x == 4:
        bd_usuarios.atualizar_cadastro()
print('Sistema Encerrado')