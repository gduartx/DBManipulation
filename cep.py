import requests
import bd_cep as bd
import sqlite3
num = '0123456789'
def formata_cep(cep):
    while len(cep) != 8:
        cep = input('CEP incorreto ou inválido, digíte novamente: ')
        numero = input('Digite o número novamente: ')
        for i in cep:
            if i not in num:
                cep = cep.replace(i,'')
    return cep


def add_cep(cep):
    numero = input('Digite o número: ')

    requisicao = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    while len(cep) != 8 or not requisicao.ok:
        cep = input('CEP incorreto ou inválido, digíte novamente: ')
        numero = input('Digite o número novamente: ')
        for i in cep:
            if i not in num:
                cep = cep.replace(i,'')
        requisicao = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    dic_requisicao = requisicao.json()

    try:
        bd.adiciona_cep(dic_requisicao, numero)
    except sqlite3.IntegrityError:
        print('CEP já adicionado')
    else:
        return 


