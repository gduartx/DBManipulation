import re

def formata_cpf(cpf):
    cpf_format = re.sub('[^0-9]','',cpf)
    return int(cpf_format)

def formata_nome(nomef):
    nomef = nomef.title()
    return nomef