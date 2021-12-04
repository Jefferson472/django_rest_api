import re
from validate_docbr import CPF


def cpf_valido(cpf):
    cpf = CPF()
    cpf.validate(cpf)
    return len(cpf) == 11


def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
